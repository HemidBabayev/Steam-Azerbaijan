from django.contrib import admin

from .models import GameShop

# Register your models here.
@admin.register(GameShop)
class GameShopAdmin(admin.ModelAdmin):
    
    list_display = ["title", "author", "price", "created_data"]
    list_display_links = ["title", "author"]
    search_fields = ["title", "author"]
    list_filter = ["created_data"]
    class Meta:
        model = GameShop
        