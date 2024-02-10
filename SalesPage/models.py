from django.db import models
# from PIL import Image

# Create your models here.

class SalesPage(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=300)
    product_price=models.CharField(max_length=200)
    product_img=models.ImageField(upload_to="images",default="default.jpg")

    def __str__(self) -> str:
        return self.product_name
    
    # def save(self, *args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img=Image.open(self.product_img.path)
    #     if img.height>200 or img.width>200:
    #         output_size=(200,200)
    #         img.thumbnail(output_size)
    #         if img.height/img.width<0.75:
    #             img=img.transpose(Image.ROTATE_270)
    #     img.save(self.product_img.path)