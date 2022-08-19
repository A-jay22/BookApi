from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    number_of_pages = models.IntegerField(default=0)
    publish_date = models.DateField(null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
