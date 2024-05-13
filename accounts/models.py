from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    

class WatchedStock(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="watched_stocks"
    )
    date = models.DateTimeField(auto_now=True)
    stock_symbol = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"
    


class Analysis(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="analysis"
    )
    date = models.DateTimeField(auto_now=True)
    stock_symbol = models.CharField(max_length=255, null=True, blank=True)
    data = models.ImageField(upload_to="media/analysis")

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:15]}"


"""
  modeller:
    custom kullanıcı modeli
    takip listesi
    çizim
    bildirim
"""