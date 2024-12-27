from django.contrib import admin
from .models import MenuItem, Order


admin.site.register(Order)



@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Removed 'photo'
