from django.db import models

# Create your models here.
class BlogPost(models.Model):
    day=models.CharField(max_length=20)
    date=models.DateField()
    title=models.CharField(max_length=1000)
    body=models.CharField(max_length=1000000)
    link=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title