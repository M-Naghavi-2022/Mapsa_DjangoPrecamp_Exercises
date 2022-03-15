from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, default = 'naghavi')
    publish_year = models.DateField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']