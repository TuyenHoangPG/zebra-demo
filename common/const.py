from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "ADMIN"
    USER = "USER"


class DayOfWeek(models.TextChoices):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
