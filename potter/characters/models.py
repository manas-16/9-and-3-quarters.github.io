from django.db import models

# Create your models here.
class character(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    nature = models.CharField(max_length=100)
    about = models.CharField(max_length=300)
    image = models.ImageField(upload_to="all_char",blank=True)
    wiki = models.CharField(max_length=300 ,default="https://en.wikipedia.org/wiki/Harry_Potter_(film_series)")
    def __str__(self):
        return self.name+'-'+self.type




class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email+'-'+self.password+'-'+self.name


class book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    dlink = models.CharField(max_length=500)
    year = models.CharField(max_length=5 ,default="1998")
    image = models.ImageField(upload_to="all_char",blank=True)
    synopsis = models.CharField(max_length=4800,default='op')


    def __str__(self):
        return self.name+'-'+self.year


class movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    trailer = models.CharField(max_length=500)
    torrent = models.CharField(max_length=500)
    year = models.CharField(max_length=4,default='2000')
    image = models.ImageField(upload_to="all_char", blank=True)
    synopsis = models.CharField(max_length=2000,default='op')
    rating = models.CharField(max_length=4,default='7.0')
    imdb = models.CharField(max_length=300 ,default="https://en.wikipedia.org/wiki/Harry_Potter_(film_series)")

    def __str__(self):
        return self.name+'-'+self.year



class bonus(models.Model):
    name = models.CharField(max_length=100)
    ebook = models.CharField(max_length=100)
    image = models.ImageField(upload_to="all_char", blank=True)
    def __str__(self):
        return self.name