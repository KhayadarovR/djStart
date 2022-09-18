from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_pub')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_pub',)
    list_filter = ('category',)

    save_on_top = True
    fields = ('id', 'views_count', 'title', 'content',  'category',  'is_pub', 'created_at', 'updated_at')
    readonly_fields = ('id', 'views_count', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
