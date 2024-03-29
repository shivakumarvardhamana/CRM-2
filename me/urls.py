"""model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from django.contrib.auth import views as auth_views
from me.models import customer
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login1,name="login"),
     path('logout/',views.logOutUser,name='logout'),
    path('',views.home,name="home"),
    path('user/',views.userpage,name="user-page"),
    path('account/',views.accountSetting,name='account'),
    path('product/',views.products,name="products"),
    path('create/<str:pk>/',views.createOrder_user,name="createordr"),
    path('customer/<str:pk_test>/',views.customer1,name="customer"),
    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.update_order,name="update_order"),
    path('delete_order<str:pk>',views.delete_order,name="delete_order"),
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html")
    ,name="reset_password"),
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"),
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
    name="password_reset_complete"),

 

]
