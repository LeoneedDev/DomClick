from django import forms
from django.forms import ModelForm
from .models import UserModel



class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('firstname','lastname','title','number','mail','tel_name','notifications','profile_id',)
