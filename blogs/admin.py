from django.contrib import admin

from blogs.models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_active", "order")
    search_fields = ("author",)


admin.site.register(Blog, BlogAdmin)
