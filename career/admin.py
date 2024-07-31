from django.utils import timezone
from django.contrib import admin
from .models import *

class ResponsibilitiesInline(admin.TabularInline):
    model = responsibilities

class ExperienceInline(admin.TabularInline):
    model = experience

class SkillInline(admin.TabularInline):
    model = skill

@admin.register(career)
class CareerAdmin(admin.ModelAdmin):
    exclude = ('last_modified',)  # Hide the last_modified field
    inlines = [
        SkillInline,
        ResponsibilitiesInline,
        ExperienceInline,
    ]
    list_display = ('title', 'category', 'startdate', 'duration', 'stipend', 'last_modified')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category__title')
    list_filter = ('category', 'startdate')
    readonly_fields = ('last_modified',)

    def save_model(self, request, obj, form, change):
        # Automatically set the last_modified field to the current timestamp
        obj.last_modified = timezone.now()
        super().save_model(request, obj, form, change)

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Certificate)
admin.site.register(Offerletter)
admin.site.register(InternshipApplication)




class Speacial_TrainingInline(admin.TabularInline):
    model = Speacial_Training
    extra = 1

class TrainingModulesInline(admin.TabularInline):
    model = Training_Modules
    extra = 1

class TrainingFAQInline(admin.TabularInline):
    model = Training_FAQ
    extra = 1

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'mode')
    search_fields = ('title', 'mode')
    inlines = [Speacial_TrainingInline, TrainingModulesInline, TrainingFAQInline]

admin.site.register(Training, TrainingAdmin)
admin.site.register(Internship_Assigned)
admin.site.register(ProjectReport)
admin.site.register(Internship_task_week)