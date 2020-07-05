from django import forms
from django.core import validators

def check_for_x(value):
    if value[0].lower() != 'x':
        raise forms.ValidationError('name should start with x')

class MyForms(forms.Form):
    name = forms.CharField()
    vname = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        all_data = super().clean()
        name = all_data['name']
        vname = all_data['vname']

        if name != vname:
            raise forms.ValidationError('names are not same ')
