from django.contrib import admin
from . import models

admin.site.register(models.Analysis)
admin.site.register(models.User)
admin.site.register(models.Notification)
admin.site.register(models.WatchedStock)


