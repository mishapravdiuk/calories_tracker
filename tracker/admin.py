from django.contrib import admin
from .models import Food, Consume

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')
    save_as=True
    save_on_top=True
    search_fields = ('name',)

class ConsumeAdmin(admin.ModelAdmin):
    list_display = ('user',)
    save_as=True
    save_on_top=True


admin.site.register(Food, FoodAdmin)
admin.site.register(Consume, ConsumeAdmin)
