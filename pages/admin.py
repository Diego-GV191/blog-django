from django.contrib import admin
from .models import Page

# configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible', )
    list_display = ('title', 'visible', 'updated_at', 'created_at')
    ordering = ('updated_at', )

# Register your models here.
admin.site.register(Page, PageAdmin)