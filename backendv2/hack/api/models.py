from pyexpat import model
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nalog_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=False)
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=30, blank=False)
    role = models.CharField(max_length=100, blank=True)

#   Owner, admin, player


class Deal(models.Model):
    id_deal = models.IntegerField(null=False)
    name_deal = models.CharField(max_length=100, null=False)
    description_deal = models.CharField(max_length=1000, null=True, blank=True)
    date_deal = models.DateTimeField(auto_now_add=True)
    owner_id = models.IntegerField(null=False)
    first_place_id = models.IntegerField(null=True, blank=True)
    second_place_id = models.IntegerField(null=True, blank=True)
    status_deal = models.CharField(null=True, blank=True)
    start_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_deal


class Lastbet(models.Model):
    last_bet_id = models.ForeignKey(Deal, null=True)
    last_date_time = models.DateTimeField(null=True)
    last_user_bet = models.IntegerField(null=True)

class Notification(models.Model):
    user_preference = models.CharField(max_length=10)  # Email/Telegram
    notification_type = models.IntegerField()
    owner_id = models.IntegerField(null=False)

    def __str__(self):
        return self.owner_id

    # 0. 5 минут до конца сессии
    # 1. окончание сессии
    # 2. подписание оферты
    # 3. подписание контракта
