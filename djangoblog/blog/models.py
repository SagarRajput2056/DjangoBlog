from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, blank=True)
    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    