from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class projects(models.Model):
    title = models.CharField(("Title"), max_length=250)
    companyname= models.CharField(("Company Name"), max_length=50)
    shortdes = models.CharField(("Short Description"), max_length=350)
    bannerimg = models.ImageField(("Banner Image"), upload_to='project/banner/')
    cardimg = models.ImageField(("Card Image"), upload_to='project/card/')
    client = models.CharField(("Client name"), max_length=250)
    hq = models.CharField(("HeadQuaters"), max_length=250)
    industry = models.CharField(("Industry"), max_length=250)
    founder = models.CharField(("Founders"), max_length=250)
    service = models.CharField(("Service"), max_length=250)
    time = models.CharField(("Time Spent"), max_length=250)
    overview = RichTextField(("overview"))
    challenges = RichTextField(("challenges"))
    result = RichTextField(("result"))
    link = models.CharField(("Project Link"), max_length=2250)

    feedback = models.TextField(("Feedback"))

    slug = models.CharField(("Slug"), max_length=250,unique=True,blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(projects, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title