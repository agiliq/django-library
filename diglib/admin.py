from diglib.models import Publisher, \
    Authors, Books, Transaction, 
from django.contrib.auth.models import User

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Books)
admin.site.register(Transaction)

