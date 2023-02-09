from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image",null=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="like")

    @property
    def fetch_comments(self):
        comment=self.comments_set.all()
        return comment

    def __str__(self):
        return self.title

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)


class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image",null=True)
    place=models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    phone=models.PositiveBigIntegerField()

