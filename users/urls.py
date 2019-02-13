from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url('submit-flag/', views.get_flag),
    path('leaderboards/', views.get_table, name='leaderboards'),
]
