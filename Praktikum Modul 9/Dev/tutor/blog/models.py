from django.db import models
from django.utils.text import slugify
from .validators import title_val

# # Create your models here.\
# class Post(models.Model):
#     title = models.CharField(max_length=20)
#     body = models.TextField()
#     # email = models.EmailField(blank=True)
#     # slug = models.SlugField(blank=True, editable=False)

#     def save(self):
#         self.slug = slugify(self.title)
#         super(Post, self).save()

# class Post(models.Model):
#     nama= models.CharField(max_length=100, unique=True)
#     alamat= models.TextField()
#     tgl_lahir = models.CharField(max_length=20)
#     email = models.EmailField(blank=True)
#     slug = models.SlugField(blank=True, editable=False)
    
#     def save(self):
#         self.slug = slugify(self.nama)
#         super(Post, self).save()

#     def __str__(self):
#         return "{}".format(self.nama)

class Post(models.Model):
    title = models.CharField(max_length=20, validators=[title_val])
    body = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return "{}".format(self.title)


    

    