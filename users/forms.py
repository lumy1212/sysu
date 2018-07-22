from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'student_id', 'grade', 'major', 'email']
        label = {'name': '','student_id':'','grade':'','major':'','email':''}

