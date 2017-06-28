from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name

class Metric(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=False, blank=False)
    value = models.IntegerField(default=0, null=False)
    weight = models.IntegerField(default=1, null=False)
    department = models.ForeignKey(Department, related_name='metrics')

    def __str__(self):
        return self.name
