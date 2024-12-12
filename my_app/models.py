from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=255)
    descryption = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    def total(self):
        return self.price*self.quantity
    def __str__(self):
        return self.name