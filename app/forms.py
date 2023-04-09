from django import forms
from app.models import *

class Topicform(forms.Form):
    topic_name=forms.CharField(max_length=100)

class Studentform(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
       # widgets={'password':forms.PasswordInput,'add':forms.Textarea}
        #help_texts={'name':'only alphabets','password':'alphabets,number and special charecters'}
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea}

class Subjectform(forms.ModelForm):
    class Meta():
        model=Subject
        fields='__all__'