"""social_networking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialapp.views import PostList,SignupView,LoginView,UserdetailView,like_view,add_comment,signout,UserprofileView,PostDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',PostList.as_view(),name="home"),
    path('register',SignupView.as_view(),name="register"),
    path('',LoginView.as_view(),name="login"),
    path('user/details/edit',UserdetailView.as_view(),name="profile"),
    path('post/<int:id>/like',like_view,name="like"),
    path('post/<int:id>/comment',add_comment,name="comment"),
    path('logout',signout,name="logout"),
    path('user/profile',UserprofileView.as_view(),name="userprofile"),
    path('post/<int:id>/delete',PostDeleteView.as_view(),name="delete"),
    # path('user/<int:id>/edit',UserdetailUpdateView.as_view(),name="editdetail"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
