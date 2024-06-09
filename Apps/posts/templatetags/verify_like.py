from django import template
from ..models import Like

register = template.Library()

@register.filter
def verify_like(post, user):
    
    is_like =  Like.objects.filter(post=post, user=user).exists()
    return is_like