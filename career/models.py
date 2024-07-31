from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from career.utils.certificate.internship.certificate_generation import generate_certificate
from career.utils.certificate.internship.offer_letter_generation import generate_offerletter
from career.utils.certificate.internship.certificate_mail import send_mail_certificate
from career.utils.certificate.internship.offerletter_mail import send_offermail_certificate
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from auth_app.models import *
# Create your models here.

class category(models.Model):
    title = models.CharField(("Name"), max_length=50)

    def __str__(self):
        return self.title
    
class career(models.Model):
    title = models.CharField(("Title"), max_length=250)
    shortdes = models.CharField(("Short description"), max_length=250)
    img = models.ImageField(("Card Image"), upload_to='career/card')
    category = models.ForeignKey(category, verbose_name=("Category"), on_delete=models.CASCADE)
    edu = models.CharField(("Education Required"), max_length=250)
    des = RichTextField(("Description"))
    mode = models.CharField(("Mode"), max_length=250)
    startdate = models.DateField(("Start date"), auto_now=False, auto_now_add=False)
    duration = models.CharField(("Duration"), max_length=50)
    no_of_weeks = models.IntegerField(("no_of_weeks"))
    last_modified = models.DateTimeField(auto_now=True)
    stipend = models.CharField(("Stipend/paid/free"), max_length=50)
    code = models.CharField(("Code"), max_length=50)
    slug = models.CharField(("Slug"), max_length=250,unique=True,blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(career, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Internship_task_week(models.Model):
    internship = models.ForeignKey(career, verbose_name=("Internship"), on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    link = models.CharField(("Link"), max_length=250)

class skill(models.Model):
    career = models.ForeignKey(career, verbose_name=("Career"), on_delete=models.CASCADE)
    name = models.CharField(("Skills"), max_length=250)
    des = models.TextField(("Des"))

class responsibilities(models.Model):
    career = models.ForeignKey(career, verbose_name=("Career"), on_delete=models.CASCADE)
    name = models.CharField(("Responsibilities"), max_length=250)
    des = models.TextField(("Des"))

class experience(models.Model):
    career = models.ForeignKey(career, verbose_name=("Career"), on_delete=models.CASCADE)
    name = models.CharField(("Experience"), max_length=250)
    des = models.TextField(("Des"))

class Certificate(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True)
    email = models.CharField(("Email ID"), max_length=250,blank=True)
    internship_for = models.ForeignKey(career, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=timezone.now)
    certificate_id = models.CharField(max_length=20, unique=True, blank=True)
    certificate_image = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            # Generate certificate_id
            internship_code = career.objects.get(slug=self.internship_for.slug).code
            year = timezone.now().year
            serial_number = Certificate.objects.filter(internship_for=self.internship_for, date_of_issue__year=year).count() + 1
            self.certificate_id = f'NEX-{internship_code}-{str(serial_number).zfill(3)}'
            self.certificate_image = generate_certificate(self.name,self.certificate_id,self.internship_for.title,self.date_of_issue)
            self.save(update_fields=['certificate_image'])
            send_mail_certificate(name=self.name,internship_for=self.internship_for,date_of_issue=self.date_of_issue,certificate_image=self.certificate_image,email=self.email)

            super().save(*args, **kwargs)

        if not self.certificate_image:
            self.certificate_image = generate_certificate(self.name,self.certificate_id,self.internship_for.title,self.date_of_issue)
            self.save(update_fields=['certificate_image'])
            send_mail_certificate(name=self.name,internship_for=self.internship_for,date_of_issue=self.date_of_issue,certificate_image=self.certificate_image,email=self.email)

            super().save(*args, **kwargs)
       
        

    def __str__(self):
        return self.certificate_id

class Offerletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(("Email ID"), max_length=250)
    internship_for = models.ForeignKey(career, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=timezone.now)
    certificate_id = models.CharField(max_length=20, unique=True, blank=True)
    certificate_image = models.CharField(max_length=250,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            # Generate certificate_id
            internship_code = career.objects.get(slug=self.internship_for.slug).code
            year = timezone.now().year
            serial_number = Offerletter.objects.filter(internship_for=self.internship_for, date_of_issue__year=year).count() + 1
            self.certificate_id = f'NEX-{internship_code}-{str(serial_number).zfill(3)}'
            self.certificate_image = generate_offerletter(self.name,certificateid=self.certificate_id,internshipfor=self.internship_for.title,date_of_issue=self.date_of_issue,email=self.email)
            self.save(update_fields=['certificate_image'])
            send_offermail_certificate(name=self.name,internship_for=self.internship_for,date_of_issue=self.date_of_issue,certificate_image=self.certificate_image,email=self.email)
            super().save(*args, **kwargs)
            
        if not self.certificate_image:
            self.certificate_image = generate_offerletter(self.name,certificateid=self.certificate_id,internshipfor=self.internship_for.title,date=self.date_of_issue,email=self.email)
            self.save(update_fields=['certificate_image'])
            send_offermail_certificate(name=self.name,internship_for=self.internship_for,date_of_issue=self.date_of_issue,certificate_image=self.certificate_image,email=self.email)

            super().save(*args, **kwargs)
       
        

    def __str__(self):
        return self.certificate_id
    
class InternshipApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    internship_for = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    convert = models.BooleanField(("Convert to intern"))

    def __str__(self):
        return self.name

class Training(models.Model):
    title = models.CharField(("Title"), max_length=50)
    des = RichTextField(("Short description"))
    duration = models.CharField(("Duration"), max_length=50)
    mode = models.CharField(("Mode"), max_length=50,choices={"Online":"Online","Offline":"Offline"})
    long_desc = RichTextField(("Long Description"))
    img = models.ImageField(("card Image"), upload_to='training')
    banner = models.ImageField(("Banner Image"), upload_to='training/banner')
    price = models.CharField(("Price"), max_length=50)


    slug = models.CharField(("Slug"), max_length=250,unique=True,blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Training, self).save(*args, **kwargs)

 

    def __str__(self):
        return self.title
    
class Speacial_Training(models.Model):
    training = models.ForeignKey(Training, verbose_name=("Training"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=50)

class Training_Modules(models.Model):
    training = models.ForeignKey(Training, verbose_name=("Training"), on_delete=models.CASCADE)
    module = models.CharField(("Module"), max_length=50)
    title = models.CharField(("Title"), max_length=50)
    desc = models.TextField(("Description"))

class Training_FAQ(models.Model):
    training = models.ForeignKey(Training, verbose_name=("Training"), on_delete=models.CASCADE)
    question = models.CharField(("Question"), max_length=2550)
    answer = models.TextField(("Answer"))

class Internship_Assigned(models.Model):
    
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    internship = models.ForeignKey(career, verbose_name=("Internship For"), on_delete=models.CASCADE)
    start_date = models.DateField(("Date"), auto_now=True)
    completed = models.BooleanField(("Completed"),default=False)
    offer_letter = models.ForeignKey(Offerletter, verbose_name=("Offerletter"), on_delete=models.CASCADE)
    assigned_id = models.CharField(("assigned_id"), max_length=50,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.assigned_id:
            get_id = Offerletter.objects.get(certificate_id=self.offer_letter.certificate_id)
            self.assigned_id = get_id
        super().save(*args, **kwargs)

class ProjectReport(models.Model):
    internship_assigned = models.ForeignKey(Internship_Assigned, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    report = models.TextField()
    submission_date = models.DateField(auto_now_add=True)
    submission = models.CharField(("Submision"),choices={"Pending":"Pending","Completed":"Completed","Rewrite":"Rewrite","Rejected":"Rejected"}, max_length=50, default="Pending")

    def __str__(self):
        return f"Week {self.week_number} report for {self.internship_assigned}"