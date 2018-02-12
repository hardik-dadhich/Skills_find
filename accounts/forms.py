from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# for signup new user with help of UserCreationForm
class UserForm(UserCreationForm):
    Register_no = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('Register_no', 'school_name', 'username', 'email' , 'state', 'village', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.Register_no = self.cleaned_data['Register_no']
        user.school_name = self.cleaned_data['school_name']
        user.state = self.cleaned_data['state']
        user.village = self.cleaned_data['village']

        if commit:
           user.save()


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].label = "Enter name here"
    self.fields['email'].label = "Enetr email"
    self.fields['password'].label = "Enter Password"
