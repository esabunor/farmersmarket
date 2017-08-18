from django import template
from oscar.apps.catalogue.models import Product, ProductImage
register = template.Library()

@register.filter
def toimage(value):
    """returns the image of a product value = product to retrieve image
    """
    image = ProductImage.objects.filter(product=value)
    return image[0].original
