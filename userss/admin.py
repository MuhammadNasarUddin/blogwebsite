from django.contrib import admin
from .models import Blogs
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    search_fields = ['title', 'author', 'date']
    list_filter = ['date', 'author']
    list_per_page = 10
    

class SummernoteBlogAdmin(SummernoteModelAdmin, BlogAdmin):
    summernote_fields = ('desc',)


admin.site.register(Blogs, SummernoteBlogAdmin)
