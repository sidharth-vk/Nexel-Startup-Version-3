from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class ProjectFeedback(models.Model):
    name = models.CharField(("Name"), max_length=250)
    comapny = models.CharField(("Company Name"), max_length=250)
    service = models.CharField(("Service done"), max_length=250)
    logo = models.ImageField(("Logo"), upload_to="feedback/company")
    des = models.CharField(("Designation"), max_length=250)
    content = RichTextField(("feedback"))
    rating = models.CharField(("Positive Integer(12345)"), max_length=50)
    slug = models.CharField(("Slug"), max_length=250,blank=True,unique=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ProjectFeedback, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    


class Team(models.Model):
    name = models.CharField(("Name"), max_length=250)
    img = models.ImageField(("Profile"), upload_to="team")
    role = models.CharField(("Role"), max_length=250)
    linkedin= models.CharField(("Linkedin Url"), max_length=250, null=True, blank=True)
    instagram= models.CharField(("instagram Url"), max_length=250, null=True, blank=True)
    twitter= models.CharField(("twitter Url"), max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    


class Terms_and_condition(models.Model):
    data = RichTextField()
    


class Privacy_policy(models.Model):
    data = RichTextField()
    

class Refund_policy(models.Model):
    data = RichTextField()
    


class ads_vertical(models.Model):
    img = models.ImageField(("Image"), upload_to="ads/vertical")


class ads_horizontal(models.Model):
    img = models.ImageField(("Image"), upload_to="ads/horizontal")



class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    


class Business(models.Model):
    business_name = models.CharField(max_length=255)
    business_description = models.TextField()
    contact_email = models.EmailField()
    business_goals = models.TextField()

    def __str__(self):
        return self.business_name