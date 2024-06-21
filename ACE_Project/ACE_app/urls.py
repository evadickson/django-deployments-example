from django.urls import path
from ACE_app import views

# For TEMPLATE TAGGING
app_name = 'ACE_app'

urlpatterns = [

    path('',views.index,name='index'),
    path('help/',views.help,name='help'),
    path('users/', views.users, name='users'),
    path('relative/', views.relative, name='relative'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),

]