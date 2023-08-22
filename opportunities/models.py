from django.db import models


from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories', blank=True, null=True)

class Opportunity(BaseModel):
    opportunity_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stipend = models.CharField(max_length=255)
    op_description = models.TextField()
    location = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    op_link = models.URLField(max_length=255)





class OpportunityImage(BaseModel):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='opportunity', blank=True, null=True)