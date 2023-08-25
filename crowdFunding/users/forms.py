from django import forms
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth import get_user_model


prefixes = ['010', '011', '012','015']  
def egNumbers(num):
    if not num.startswith(tuple(prefixes)) or len(num) != 11:
        raise forms.ValidationError("Please Enter an Egyptian Number")


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    mobile = forms.CharField(validators =[egNumbers])

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email','mobile','picture', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)        