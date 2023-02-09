from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from socialapp.models import Posts,Userprofile


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","image","description"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3}),        
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }

class UserdetailForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=[
            "place",'dob','phone',"image"
        ]


        widgets={
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.TextInput(attrs={"class":"form-control"}), 
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }

class UserdetaileditForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=[
            "place",'dob','phone'
        ]


        widgets={
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.TextInput(attrs={"class":"form-control"}), 
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }