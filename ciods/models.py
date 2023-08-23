from django.db import models
from PIL import Image

class Ciods(models.Model):
    name = models.CharField(max_length = 255,null = True)
    designation = models.CharField(max_length = 255,null = True)
    Job_descritption = models.CharField(max_length = 2000,null = True)
    github_link = models.CharField(max_length = 255,null = True, blank = True)
    google_plus_link = models.CharField(max_length = 255,null = True, blank = True)
    linked_in_link = models.CharField(max_length = 255,null = True, blank = True)
    image = models.ImageField(upload_to = 'profiles/', null = True)
    level = models.IntegerField(default = 3)

    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path) # Open image using self
        new_img = (400, 400)
        img.thumbnail(new_img)
        img.save(self.image.path)  # saving image at the same path

    def __str__(self):
        return self.name

class Publication(models.Model):
    publication = models.TextField(max_length = 5000, null = True)
    link = models.CharField(max_length = 1000, null = True, blank = True)
    journal = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.publication



