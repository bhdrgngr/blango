from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)