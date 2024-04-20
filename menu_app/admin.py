from django.contrib import admin

# Register your models here.
from .forms import MenuItemForm
from .models import Menu, MenuItem

class ItemInline(admin.StackedInline):
    model = MenuItem
    extra = 0
    fields = ['menu', 'title', 'parent', 'href', 'named_url']

class MenuAdmin(admin.ModelAdmin):
    inlines = ItemInline,

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ('menu', 'title', 'parent', 'href', 'named_url')
    fields = ['menu', 'title', 'parent', 'href', 'named_url']
    inlines = ItemInline,

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)