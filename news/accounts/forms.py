from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, CustomerPhoto

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", ) + UserCreationForm.Meta.fields + ("email", "age", )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", )

class CustomerPhotoForm(forms.ModelForm):
    class Meta:
        model = CustomerPhoto
        fields = ( "photo", "user", )
        widgets = {'user': forms.HiddenInput()}