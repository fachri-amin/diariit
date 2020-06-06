from django.contrib import admin

# Register your models here.

from .models import Post

class slugPost(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update'
    ]

admin.site.register(Post, slugPost)
