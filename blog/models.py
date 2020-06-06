from django.db import models
from django.utils.text import slugify

from .validators import clean_judul

# Create your models here.

class Post(models.Model):
    judul = models.CharField(
        max_length=200,
        validators=[
            clean_judul,
        ],
    )
    body = models.TextField()
    category = models.CharField(
        max_length=100,
        default='no-category',
        choices=(
            ('Blog','blog'),
            ('No-Category','no-category'),
            ('Jurnal','jurnal'),
            ('Berita','berita'),
        )    
    )
    publish = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)

    def save(self, **kwargs): #**kwargs ini penting
        self.slug = slugify(self.judul)
        super(Post, self).save()


#superuser
#admin
#admin1234