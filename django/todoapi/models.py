from django.db import models

class activities(models.Model):  
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 150)
    tag = models.TextField(max_length=500)

    class Meta:
        db_table = 'activities'
        ordering = ['id']

    def __str__(self):
        return self.name


class tags(models.Model):
    tag_name = models.CharField(max_length = 25)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.tag_name