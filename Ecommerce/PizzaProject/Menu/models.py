from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    #db index - spped up searching process for databases.
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Menu:product_list_by_category',args=[self.slug])


class Product(models.Model):
    #related_name - to get all the instances of
    #Product model that have relation to this current
    #category
    category = models.ForeignKey(Category,related_name='products',
    on_delete = models.CASCADE)

    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)#to improve performance while quering.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Menu:product_detail',args=[self.id,self.slug])
