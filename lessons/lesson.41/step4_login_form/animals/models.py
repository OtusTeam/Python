from django.db import models


class Animal(models.Model):
    # Имя: Борис
    name = models.CharField(max_length=32)
    # Семейство: Медведь
    family = models.CharField(max_length=32)
    # Вид: Белый
    kind = models.CharField(max_length=32)
