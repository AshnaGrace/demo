from django import forms
from demo_app.models import shop
class Todoform(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','img','price']