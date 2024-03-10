from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50)  # e.g., user, trainer, admin

    def __str__(self):
        return f"{self.username} ({self.role})"
class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    availability = models.IntegerField()  # Max number of participants

    def __str__(self):
        return f'{self.name} {self.description} {self.trainer} {self.availability}'
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # e.g., cardio, strength
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.type})"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        details = f"Reservation for {self.user}"
        if self.training:
            details += f" | Training: {self.training}"
        if self.equipment:
            details += f" | Equipment: {self.equipment}"
        return f'{details}, {self.date}'
