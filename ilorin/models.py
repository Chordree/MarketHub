from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# remeber to add price and modify description 
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'    # see the effect of this meta data class 

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    # see to cascade the category on delete 

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(default=0.00)
    # add price later this week 

    def __str__(self):
        return self.description
# add price to this description module 
# see what this verbose name does 