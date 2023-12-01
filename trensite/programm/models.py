from django.db import models


class UserPayment(models.Model):
    card_number = models.CharField(max_length=19, verbose_name="Номер карты", error_messages='Неправильная карта')
    expiration_date = models.CharField(max_length=5, verbose_name="Срок действительности карты", error_messages='Срок действительности неверен')
    cvv_2 = models.CharField(max_length=3, verbose_name="Код безопасности", error_messages='Введите CVV')
    username = models.CharField(max_length=150, verbose_name="Имя владельца", error_messages='Введите ваше имя и фамилию')
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", error_messages='Неверный номер')
    email = models.EmailField(verbose_name="Email", error_messages='Введите ваш email')

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
