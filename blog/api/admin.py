from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_per_page = 1
    search_fields = ('name','description')
    ordering = ('name',)
    
admin.site.register(Item, ItemAdmin)