from django import forms
from django.core import validators
from basic_app.models import Question, UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email',"password")

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Name need to start with Z")

class New_QuestionForm (forms.ModelForm):
    class Meta():
        model = Question
        fields = "__all__"


class FormName (forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your e-mail again...')
    text = forms.CharField(widget=forms.Textarea)

    def clean (self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure u enter verify_email correctly...')
