from django.contrib import admin

from .models import User, Deal, Notification

admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Notification)
