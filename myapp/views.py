from django.shortcuts import render
from myapp import forms
# Create your views here.

def myforms(request):

    form = forms.MyForms()

    if request.method == "POST":
        form = forms.MyForms(request.POST)

        if form.is_valid():
            print('something!')
            print('name is: '+form.cleaned_data['name'])
            print('text is: '+form.cleaned_data['text'])
            print('password is: '+form.cleaned_data['password'])

    return render(request, 'forms.html', {'form':form})
