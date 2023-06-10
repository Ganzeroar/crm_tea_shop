from django.db import models


class NotificationInfo(models.Model):
    telegram_user_id = models.CharField(max_length=20, verbose_name='Телеграм user_id')

    class Meta:
        verbose_name = 'Telegram id для уведомлений'
        verbose_name_plural = 'Telegram id для уведомлений'

    def __str__(self):
        return self.telegram_user_id
