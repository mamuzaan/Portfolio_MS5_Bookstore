from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("products:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_creator")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, default="default.png")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
