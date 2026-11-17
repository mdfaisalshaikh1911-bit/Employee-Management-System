
from django import forms
from myapp.models import Users


class UserForm(forms.ModelForm):

    class Meta:
        model = Users

        fields = [ 'name', 'salary', 'designation', 'phone_number', 'company_name', 'department', 'role', 'age', 'dob', 'gender', ]

        widgets = { 'dob': forms.DateInput(attrs={'type': 'date'}) }