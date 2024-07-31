
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class service(models.Model):
    name = models.CharField(("Title"), max_length=250)
    des = models.TextField(("Short description"))
    img = models.ImageField(("Service image"), upload_to='Service/card')
    approach = RichTextField(("Approach"))
    slug = models.CharField(("Slug"), max_length=250,unique=True,blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(service, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class service_benefits(models.Model):
    service = models.ForeignKey("service", verbose_name=("service"), on_delete=models.CASCADE)
    benifits = models.CharField(("benifits"), max_length=250)
    

class service_work(models.Model):
    service = models.ForeignKey("service", verbose_name=("service"), on_delete=models.CASCADE)
    slno = models.CharField(("Serial no"), max_length=50)
    work = models.CharField(("work"), max_length=250)
    des = models.CharField(("des"), max_length=2250)

class solution(models.Model):
    service = models.ForeignKey("service", verbose_name=("service"), on_delete=models.CASCADE)
    work = models.CharField(("Solution"), max_length=250)
    des = models.CharField(("des"), max_length=2250)
