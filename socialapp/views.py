from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,ListView,View,UpdateView
from socialapp.forms import RegistrationForm,LoginForm,PostForm,UserdetailForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from socialapp.models import Posts,Userprofile,Comments
from socialapp.models import Userprofile
from django.utils.decorators import method_decorator

# Create your views here.
def sign_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args, **kwargs)
    return wrapper


class SignupView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name: str="register.html"
    success_url=reverse_lazy("login")
    
class LoginView(FormView):
    form_class=LoginForm
    template_name: str="login.html"
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            usr=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=usr,password=pwd)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":form})



   

    
@method_decorator(sign_required,name="dispatch")
class PostList(CreateView,ListView):
    model=Posts
    template_name: str="base.html"
    context_object_name="posts"
    form_class=PostForm
    success_url=reverse_lazy("home")

    def get_queryset(self):
        return Posts.objects.all().exclude(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data(**kwargs)
        context["userd"] = Userprofile.objects.get(user=self.request.user)
        return context
    
    def form_valid(self, form):
        # form doesnot contain info about user we have to give it seprately
        form.instance.user=self.request.user 
        return super().form_valid(form)
    





@sign_required
def like_view(request,*args, **kwargs):
    pos_id=kwargs.get("id")
    pos=Posts.objects.get(id=pos_id)
    pos.like.add(request.user)
    pos.save()
    return redirect("home")

@sign_required
def add_comment(request,*args, **kwargs):
    post_id=kwargs.get("id")
    pos=Posts.objects.get(id=post_id)
    com=request.POST.get("answer")
    pos.comments_set.create(comment=com,user=request.user)
    return redirect("home")

@sign_required
def signout(request,*args, **kwargs):
    logout(request)
    return redirect("login")

@method_decorator(sign_required,name="dispatch")           
class UserprofileView(ListView):
    model=Posts
    template_name: str="userprofile.html"
    context_object_name="posts"

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(UserprofileView,self).get_context_data(**kwargs)
        context["userd"] = Userprofile.objects.get(user=self.request.user)
        return context

@method_decorator(sign_required,name="dispatch")
class PostDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        Posts.objects.filter(id=id).delete()
        return redirect("userprofile")


class PostDetailView(ListView):
    model=Posts
    template_name: str="postdetail.html"
    context_object_name="posts"

@method_decorator(sign_required,name="dispatch")           
class UserdetailView(CreateView):
    model=Userprofile
    template_name: str="userprofiledetails.html"
    form_class=UserdetailForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        # form doesnot contain info about user we have to give it seprately
        form.instance.user=self.request.user 
        return super().form_valid(form)