from django.contrib import admin

# Register your models here.
from rango.models import category, page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(category, CategoryAdmin)
admin.site.register(page, PageAdmin)
admin.site.register(UserProfile)