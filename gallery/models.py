from django.db import models


class imggal(models.Model):
    imgtitle=models.CharField(max_length=50)
    imgdesc=models.CharField(max_length=20)
    image=models.ImageField(upload_to='files/covers')

    




    # image=models.ImageField(upload_to='media/images/')