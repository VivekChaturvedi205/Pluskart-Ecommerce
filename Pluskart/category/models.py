from django.db import models
from django.urls import reverse
# Create here model for category

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    category_img=models.ImageField(upload_to='Images/Categories', blank=True, null=True)    

    class Meta:
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

