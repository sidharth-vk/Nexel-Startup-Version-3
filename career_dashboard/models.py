from django.db import models
from ckeditor.fields import RichTextField  # Import RichTextField from ckeditor

# Create your models here.


class Resources(models.Model):
    title = models.CharField(("Category"), max_length=250)
    logo = models.ImageField(("File"), upload_to="resources/category")
    folder = models.ImageField(("folder"), upload_to="resources/folder")

    def __str__(self):
        return self.title


class Resources_file_data(models.Model):
    resources = models.ForeignKey(Resources, verbose_name=("Resources"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=250)
    code = RichTextField(("Code"))
    des = RichTextField(("Explanation"))
    data = models.CharField(("Github Link"), max_length=500)

  


class Resources_video_data(models.Model):
    resources = models.ForeignKey(Resources, verbose_name=("Resources"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=250)
    data = models.CharField(("Github Link"), max_length=500)


class Resources_Folder_data(models.Model):
    resources = models.ForeignKey(Resources, verbose_name=("Resources"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=250)
    data = models.CharField(("Github Link"), max_length=500)