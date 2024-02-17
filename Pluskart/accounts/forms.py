from django import forms
from accounts.models import Account

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm_password'}))

    class Meta:
        model = Account
        fields = ['first_name','last_name','email','mobile','password']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['mobile'].widget.attrs['placeholder'] = 'Enter Mobile No'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
