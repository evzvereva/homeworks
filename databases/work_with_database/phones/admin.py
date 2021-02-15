from django.contrib import admin

# Register your models here.
from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass
