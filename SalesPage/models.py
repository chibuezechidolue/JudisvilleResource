from django.db import models

# Create your models here.

class SalesPage(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=300)
    product_price=models.CharField(max_length=200)
    product_img=models.ImageField(upload_to="images",default="default.jpg")

    def __str__(self) -> str:
        return self.product_name