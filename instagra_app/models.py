from django.db import models

# Create your models here.
class UserProfile(models.Model):
    photo = models.ImageField(upload_to = 'profile/images/')
    bio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.bio

class imageIn(models.Model):
    name = models.CharField(max_length=30)
    caption = models.TextField()
    image_url = models.ImageField(upload_to = 'images/')
    comments = models.TextField( blank=True)
    likes = models.TextField( blank=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name