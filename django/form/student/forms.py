from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']


    # def class_age(self):
    #     age=self.cleaned_data.get("age")

