from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'is_staff', 'is_active', 'date_joined')


    filter_horizontal = []
    list_filter = []
    ordering = ['id']
    readonly_fields = ['password']


# Register your models here.
admin.site.register(Account,AccountAdmin)


