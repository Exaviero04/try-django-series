from django import  forms
from.models import db_project
class productform(forms.ModelForm) :
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"how you doing"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":10 ,"cols":20,"placeholder": "no ides what i am  doing" }))
    class Meta:
        model = db_project
        fields = ['title', 'price', 'description']
