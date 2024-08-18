from django.db import models
from django.utils import timezone

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=100)
    meter_number = models.IntegerField(blank=False)
    amount_to_buy = models.IntegerField(blank=False)
    request_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' | ' + str(self.meter_number) + ' | ' + str(self.amount_to_buy)