from dataclasses import field
from .models import customer, order
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model=customer
        fields='__all__'
        exclude=['user']
class OrderForm(ModelForm):
    class Meta:
        model=order
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class Order_1(ModelForm):
    class Meta:
        model=order
        fields='__all__'
        exclude=['customer','status']