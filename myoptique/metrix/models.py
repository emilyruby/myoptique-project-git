from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    part_of = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Metric(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=False, blank=False)
    department = models.ForeignKey(Department, related_name='metrics')
    curr_val = models.CharField(default='0%', max_length=10, null=False)
    color = models.CharField(default='green', max_length=10, null=False)

    def __str__(self):
        return self.name
