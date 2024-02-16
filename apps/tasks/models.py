from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.users.models import User
from common.const import DayOfWeek
from common.model import TimeStampMixin

# Create your models here.


class Task(TimeStampMixin):
    week_number = models.IntegerField(null=False)
    project_name = models.CharField(null=False)
    task_name = models.CharField(null=False)
    day_of_week = ArrayField(models.TextField(choices=DayOfWeek.choices), null=True)
    hour = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, related_name="user_assigned_task"
    )

    class Meta:
        db_table = "tasks"
