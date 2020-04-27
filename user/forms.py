from django import forms

from .models import *



class MyPreferenceForm(forms.ModelForm):
    class Meta:
        model = MyPreference
        fields = ('id','country', 'city', 'location')
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'required': True,'cols': 80, 'rows': 10}),
        #     'parent': forms.Select(attrs={'class': 'form-control'}),
        #     'background_image': forms.FileInput(attrs={'class': 'form-control', 'required': True, 'onchange':'loadFile(event)'}),

        # }

        # widgets = {
        #     'location': forms.Select(choices=CHOICES, attrs={'class': 'form-control', 'required': True}),
           
        # }