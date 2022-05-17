from django.db import models

class Characters(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Inventory(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Donate(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Signup(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

