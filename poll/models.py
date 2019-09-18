from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to="products")
    created = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
