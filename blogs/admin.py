from django.contrib import admin
from .models import Category, Author, Tag, BlogPost, BlogPostImage, BlogPostTag
from ckeditor.widgets import CKEditorWidget
from django import forms

# Custom form for BlogPost admin to use CKEditor
class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'

# Inline for BlogPostImage in BlogPost admin
class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1

# Inline for BlogPostTag in BlogPost admin
class BlogPostTagInline(admin.TabularInline):
    model = BlogPostTag
    extra = 1

# Admin classes
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'published_date', 'category', 'image', 'read_time', 'likes', 'comments', 'content',"quotes","quoteauthor")
        }),
    )
    list_display = ('title', 'author', 'published_date')
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'author__name')
    inlines = [
        BlogPostImageInline,
        BlogPostTagInline,
    ]

@admin.register(BlogPostImage)
class BlogPostImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post')
    list_filter = ('post',)

@admin.register(BlogPostTag)
class BlogPostTagAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'tag')
    list_filter = ('tag',)

