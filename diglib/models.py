from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag


class Publisher(models.Model):

    name = models.CharField(max_length=200)
    basic_info = models.CharField(max_length=200)
    number_of_books_owned = models.DecimalField(max_digits=10,
            decimal_places=0)

    def __unicode__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=200)
    basic_info = models.CharField(max_length=200)
    number_of_books_owned = models.DecimalField(max_digits=10,
            decimal_places=0)

    def __unicode__(self):
        return self.name


class Books(models.Model):

    title = models.CharField(max_length=200)
    number_of_pages = models.DecimalField(max_digits=10,
            decimal_places=0)
    isbn_number = models.DecimalField(max_digits=9, decimal_places=0)
    author = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    number_of_upvotes = models.DecimalField(max_digits=9,
            decimal_places=0)
    number_of_downvotes = models.DecimalField(max_digits=9,
            decimal_places=0)
    read_by = models.ManyToManyField(User)
    tags = TagField(null=True, blank=True)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

    def __unicode__(self):
        return self.title


class Transaction(models.Model):

    usr = models.ForeignKey(User)
    book = models.ForeignKey(Books)
    date_issued = models.DateField(auto_now=False, auto_now_add=False)
    date_returned = models.DateField(auto_now=False, auto_now_add=False)
