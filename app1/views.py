from django import forms

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app1.models import UserInfo


def index(request):
    form = MyModelForm()
    return render(request,"index.html",{"form":form})

class MyModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        #将需要显示的字段，变量写在这里
        fields = ["name","password","age"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }
    def __init__(self):
        super.__init__()
        #name就是fields，field就是字段对象
        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}



