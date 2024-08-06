from django.conf import settings
from django.db import models

# Create your models here.
class Yarn(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=255)
    makeup = models.CharField(max_length=255)
    price = models.IntegerField(verbose_name="cost(R) per skein")
    weight = models.IntegerField(verbose_name="weight(g) per skein")
    in_stock = models.IntegerField(verbose_name="quantity stocked")
    img_url = models.CharField(verbose_name="image location", max_length=255)
    
    
    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name="date published")
    content = models.TextField(default="N/A")
    
    
    def __str__(self):
        return f"{self.author}"
