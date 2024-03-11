from django.db import models

# Create your models here.
class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    char_field = models.CharField(max_length=255)
    number = models.IntegerField()
    agreed = models.BooleanField()
    name = models.CharField(max_length=50)
    published = models.DateTimeField()
    email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    price = models.PositiveBigIntegerField()
    slug = models.SlugField()
    time_in_day = models.TimeField()
    url = models.URLField()
    # image_field = models.ImageField(upload_to='images/')
    # json_field = models.JSONField()