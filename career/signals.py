from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Internship_Assigned)
def create_project_reports(sender, instance, created, **kwargs):
    if created:
        no_of_weeks = instance.internship.no_of_weeks
        for week in range(1, no_of_weeks + 1):
            ProjectReport.objects.create(internship_assigned=instance, week_number=week)

# @receiver(post_save, sender=career)
# def create_internship_task(sender, instance, created, **kwargs):
#     if created:
#         no_of_weeks = instance.internship.no_of_weeks
#         for week in range(1, no_of_weeks + 1):
#             Internship_task_week.objects.create(internship=instance, week_number=week)
