from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review, Comment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('content', 'created_at', 'review')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)