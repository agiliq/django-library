from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from django.core.urlresolvers import reverse

class Publisher(models.Model):

    name = models.CharField(max_length=200)
    basic_info = models.CharField(max_length=200)
    number_of_books_published = models.DecimalField(max_digits=10,
            decimal_places=0, default=1)


    def __unicode__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=200)
    basic_info = models.CharField(max_length=200)
    number_of_books_authored = models.DecimalField(max_digits=10,
            decimal_places=0, default=1)
    
    def __unicode__(self):
        return self.name


class Books(models.Model):

    title = models.CharField(max_length=200)
    number_of_pages = models.DecimalField(max_digits=10,
            decimal_places=0)
    isbn_number_10 = models.DecimalField(max_digits=15, 
                                   decimal_places=0, null=True, blank=True)
    isbn_number_13 = models.DecimalField(max_digits=15, 
                                   decimal_places=0, null=True, blank=True)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    small_thumbnail = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)
    number_of_upvotes = models.DecimalField(max_digits=9,
            decimal_places=0, default=0)
    number_of_downvotes = models.DecimalField(max_digits=9,
            decimal_places=0, default=0)
    read_by = models.ManyToManyField(User, null=True, blank=True)
    tags = TagField(null=True, blank=True)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("detail", {'var_name':"book", 'var_id':self.id})


class Transaction(models.Model):

    usr = models.ForeignKey(User)
    book = models.ForeignKey(Books)
    date_issued = models.DateField(auto_now=False, auto_now_add=False)
    date_returned = models.DateField(auto_now=False, auto_now_add=False)
