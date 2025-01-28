from django.db import models
from django.contrib.auth.models import User

class ReceipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    receipe_name = models.CharField(max_length=500)
    receipe_description  = models.TextField()
    receipe_image = models.ImageField(upload_to="Image-receipe")
    receipe_view_count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    objects = ReceipeManager()
    admin_objects = models.Manager()

    def __str__(self):
        return self.receipe_name