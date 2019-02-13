from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users.models import Flag, CustomUser
from .forms import CustomUserCreationForm
import django_tables2 as tables
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['username', 'score']


class SimpleTable(tables.Table):
    class Meta:
        model = CustomUser
        template_name = "django_tables2/bootstrap.html"


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = SimpleTable
    model = CustomUser
    template_name = 'template.html'
    filterset_class = UserFilter


def get_table(request):
    table = SimpleTable(CustomUser.objects.values('username', 'score'))
    table.exclude = ('password', 'id', 'last_login', 'is_superuser',
        'first_name', 'last_name', 'email', 'is_staff', 'is_active',
        'date_joined',)
    table.order_by = '-score'
    return render(request, 'table.html', {'table': table})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def get_flag(request):
    if (request.method == 'POST' and 'flag' in request.POST):
        subm_username = request.user.username
        subm_flag = request.POST['flag']
        print("Flag:", subm_flag, subm_username)
        subm_user = CustomUser.objects.get(username=subm_username)
        try:
            flag_obj = Flag.objects.get(flag=subm_flag)
            if not flag_obj.solved_users.get_queryset().filter(username=subm_username):
                subm_user.increase_score(flag_obj.score)
                flag_obj.solved_users.add(subm_user)
                subm_user.save()
                message = "Flag submitted successfully"
                return render(request, 'home.html', {'message': message})
            else:
                message = "You have already submitted this flag"
                return render(request, 'home.html', {'message': message})
        except Flag.DoesNotExist:
            message = "You submitted wrong flag"
            return render(request, 'home.html', {'message': message})

    else:
        return render(request, 'home.html')
