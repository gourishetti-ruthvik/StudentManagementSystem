from django import forms
from .models import Task, StudentList, Contact


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','email','address']