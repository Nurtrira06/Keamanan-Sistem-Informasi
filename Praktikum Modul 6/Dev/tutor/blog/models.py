from django.db import models
from django.utils.text import slugify

# Create your models here.\
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    # email = models.EmailField(blank=True)
    # slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
