from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import userProfileInfo
class forName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class userprofileForm(forms.ModelForm):
    class Meta():
        model = userProfileInfo
        fields = ('portfolio_site','profile_pic')