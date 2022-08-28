from urllib import request
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    category        =   models.CharField(max_length=255,db_index=True)
    slug            =   models.SlugField(max_length=255,unique=True)
    description     =   models.TextField()
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='Category_created_id')
    created_ip      =   models.GenericIPAddressField(blank=True,null=True)
    modified_date   =   models.DateTimeField(auto_now=True)
    modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='Category_modified_id')
    modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
    record_status   =   models.CharField(max_length=255,default='created')    

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self): 
        return reverse('productsCategory:categories', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        return super().save(*args, **kwargs)

class SubCategory(models.Model):
    category            =   models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category')
    sub_category        =   models.CharField(max_length=255,db_index=True)
    slug                =   models.SlugField(max_length=255,unique=True)
    description         =   models.TextField()
    is_active           =   models.BooleanField(default=True)
    created_date        =   models.DateTimeField(auto_now_add=True)
    created_id          =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='ProductSubCategory_created_id')
    created_ip          =   models.GenericIPAddressField(null=True, blank=True,)
    modified_date       =   models.DateTimeField(auto_now=True)
    modified_id         =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='ProductSubCategory_modified_id')
    modified_ip         =   models.GenericIPAddressField(null=True, blank=True,)
    record_status       =   models.CharField(max_length=255,default='created')    


    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name_plural = 'sub category'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sub_category)
        return super().save(*args, **kwargs)

class Size(models.Model):
    category            =   models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True,related_name='product_category_size')
    Size                =   models.CharField(max_length=300)
    slug                =   models.SlugField(max_length=255,unique=True,null=True, blank=True,)
    discription         =   models.TextField(blank=True,null=True)
    is_active           =   models.BooleanField(default=True)
    created_date        =   models.DateTimeField(auto_now_add=True)
    created_id          =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='Size_created_id')
    created_ip          =   models.GenericIPAddressField(null=True, blank=True,)
    modified_date       =   models.DateTimeField(auto_now=True)
    modified_id         =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='Size_modified_id')
    modified_ip         =   models.GenericIPAddressField(null=True, blank=True,)
    record_status       =   models.CharField(max_length=255,default='created')


    def __str__(self):
        return self.Size

    class Meta:
        verbose_name_plural = 'Size'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Size)
        return super().save(*args, **kwargs)



class Brand(models.Model):
    brand_category            =   models.ManyToManyField(Category,related_name='brand_category')
    title               =   models.CharField(max_length=300)
    slug                =   models.SlugField(max_length=255,unique=True,null=True, blank=True,)
    brand_images        =   models.ImageField(upload_to='brands/', null=True, blank=True,)
    discription         =   models.TextField(blank=True,null=True)
    is_active           =   models.BooleanField(default=True)
    # created_date        =   models.DateTimeField(auto_now_add=True)
    # created_id          =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='Brand_created_id')
    # created_ip          =   models.GenericIPAddressField()
    # modified_date       =   models.DateTimeField(auto_now=True)
    # modified_id         =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='Brand_modified_id')
    # modified_ip         =   models.GenericIPAddressField()
    # record_status       =   models.CharField(max_length=255,default='created')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'brands'   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)