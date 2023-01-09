from django import forms
from .models import Manager, Mentor, Student


class CreateManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"


class CreateMentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = "__all__"


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
