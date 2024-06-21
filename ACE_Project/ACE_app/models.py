from django.db import models
from django.contrib.auth.models import User

# Create your models here. store data models, the entities and relationships
class UserProfileInfo(models.Model):
    # Extending the User class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # username is one of the default attributes of the User
        return self.user.username


class Topic(models.Model):
    top_name = models.CharField(max_length=264)

    #string representation of model for easy printing out
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    
class User(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
