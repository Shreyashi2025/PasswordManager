from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Passwd_Manager, User

class ManageForm(forms.ModelForm):
    class Meta:
        model = Passwd_Manager
        fields = ["site_name","site_url","email","passwd"]