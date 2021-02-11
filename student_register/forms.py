from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:    
        model = Student
        fields = ('fullname','mobile','stu_Code','branch')
        labels = {
            'fullname':'Full Name',
            'stu_Code':'STU. Code'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['branch'].empty_label = 'Select'
        self.fields['stu_Code'].required = False