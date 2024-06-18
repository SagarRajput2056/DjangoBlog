from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=150, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, blank=True)
    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name


    