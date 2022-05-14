from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField
    is_deleted = models.BooleanField(default=False)
    deletion_comment = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
