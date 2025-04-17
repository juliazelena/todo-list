from django.contrib import admin

from catalog.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["content", ]
    list_filter = ["is_done", ]
    search_fields = ["tag", ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", ]
