from django.db import models


class Coffee(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2883)


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=10,null=NameError)
    location = models.CharField(max_length=255)
    upi = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

