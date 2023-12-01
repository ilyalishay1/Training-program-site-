from django.contrib import admin
from .models import UserPayment


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'username', 'email')
    search_fields = ('username', 'email')


admin.site.register(UserPayment, UserPaymentAdmin)
