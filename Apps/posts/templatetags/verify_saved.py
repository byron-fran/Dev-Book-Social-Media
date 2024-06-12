from django import template
from ..models import Saved

register = template.Library()

@register.filter
def verify_saved(post, user):
    
    is_saved =  Saved.objects.filter(post=post, user=user).exists()
    
    return is_saved