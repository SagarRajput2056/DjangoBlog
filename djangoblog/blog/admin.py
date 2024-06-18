from django.contrib import admin
from  .models import Post, Category, Comment
# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']
    readonly_fields = ['name', 'email', 'body']
    extra = 0

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline,]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title',]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'body']
    list_display = ['name', 'email', 'post', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

