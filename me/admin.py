from django.contrib import admin

# Register your models here.

from.models import customer,order,product,Tag

admin.site.register(customer)
admin.site.register(Tag)
admin.site.register(product)
admin.site.register(order)

