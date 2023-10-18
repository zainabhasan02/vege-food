from django.db import models


# Create your models here.
class Blog(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField()
    order = models.IntegerField()
    blog_img = models.ImageField(upload_to='blog_images', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
