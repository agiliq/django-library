from django.contrib.auth.models import User
from django.contrib import admin

from diglib.models import Publisher,\
    Author, Books, Transaction

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Books)
admin.site.register(Transaction)

