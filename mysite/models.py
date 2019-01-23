from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
