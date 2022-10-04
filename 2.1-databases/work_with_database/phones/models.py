from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name')
