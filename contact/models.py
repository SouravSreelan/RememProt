from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length = 100 )
    email = models.EmailField(max_length = 100 )
    message = models.CharField(max_length = 255 )

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = 'Contacts'
