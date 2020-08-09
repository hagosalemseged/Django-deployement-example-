from django.urls import path
from first_app import views

urlpatterns = [ 
path('',views.index,name="index"), 
path('formPage/',views.redirect_to_form,name='formName'),   
path('register/',views.registration_form,name='register'),
path(r'user-login/',views.user_login,name='user_login'),
]