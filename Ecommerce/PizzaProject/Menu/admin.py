from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

#prepopulated_fields are used to specify fields where the value
# is automatically set usig the value of other fields.

#note that any filed in the list editable
#must also be present in the list_display
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
    'available','description', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available','description']
    prepopulated_fields = {'slug': ('name',)}
