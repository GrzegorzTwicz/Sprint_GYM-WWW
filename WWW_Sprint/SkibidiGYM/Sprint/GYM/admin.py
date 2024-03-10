from django.contrib import admin

from .models import User, Trainer, Training, Equipment, Reservation

# Register your models here.
admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Training)
admin.site.register(Equipment)
admin.site.register(Reservation)

