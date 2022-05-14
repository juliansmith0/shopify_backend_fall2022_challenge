from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    deletion_comment = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name
