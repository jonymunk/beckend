from django.db import models

# Create your models here.


class Employee(models.Model):
    full_name = models.Charfield(max_length=255, null=False)
    position = models.Charfield(max_length=255, null=False)
    salary = models.Integerfield(choices=salary.choices)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.full_name)
