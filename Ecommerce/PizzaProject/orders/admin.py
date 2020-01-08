from django.contrib import admin
from .models import Order,OrderItem

# InlineModelAdmin class haqs 2 subclasses
# tabular inline and stackeinline.
#
class OrderitemInLine(admin.TabularInline):
    model=OrderItem # required field
    raw_id_fields = ['product'] # to have a new window opened as a list
    # inside dropdown .comment this line to see the changes.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','username','email','paid','created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderitemInLine]
