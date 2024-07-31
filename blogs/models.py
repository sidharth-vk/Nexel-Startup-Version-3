from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField  # Import RichTextField from ckeditor
from django.utils.text import slugify  # Import slugify for creating slugs

# Category model (unchanged)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Author model (unchanged)
class Author(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.name

# Tag model (unchanged)
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# BlogPost model with RichTextField for content and SlugField
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    content = RichTextField()  # Use RichTextField instead of TextField
    image = models.ImageField(upload_to='blog_images/')
    read_time = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    quotes = models.TextField(("Quote"),null=True,blank=True)
    quoteauthor = models.CharField(("Quote Author"), max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=255, unique=True,)  # Add SlugField for SEO-friendly URLs

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate slug if it's not set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Model for images in the blog post (optional, for multiple images)
class BlogPostImage(models.Model):
    post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Image for {self.post.title}"

# Model for tags related to the blog post (many-to-many)
class BlogPostTag(models.Model):
    post = models.ForeignKey(BlogPost, related_name='tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag.name} - {self.post.title}"