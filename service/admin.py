from django.contrib import admin
from .models import service, service_benefits, service_work,solution

class ServiceBenefitsInline(admin.TabularInline):
    model = service_benefits

class ServiceWorkInline(admin.TabularInline):
    model = service_work

class SolutionWorkInline(admin.TabularInline):
    model = solution

class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        ServiceBenefitsInline,
        ServiceWorkInline,
        SolutionWorkInline,
    ]

admin.site.register(service, ServiceAdmin)
