from django import template
from products.models import Product

register = template.Library()

@register.filter
def get_category_count(category):
	return filter_by_category(category).count()

@register.filter
def filter_by_category(category):
	return Product.objects.all().filter(categories__title=category)