from django.db import models

# Create your models here.
class ImageUploadForm(models.Model) : 
    image = models.ImageField(upload_to='images/') 
