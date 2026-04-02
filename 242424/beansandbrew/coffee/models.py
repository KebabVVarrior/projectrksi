from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('espresso', 'Эспрессо'),
        ('alternative', 'Альтернатива'),
        ('author', 'Авторские'),
        ('dessert', 'Десерты'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.TextField()
    working_hours = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)


class Message(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)