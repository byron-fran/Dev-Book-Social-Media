from django.db import models
from model_utils.models import TimeStampedModel
import uuid
from users.models import User
from posts.models import Post

# Create your models here.
class Comment(TimeStampedModel):
    
    id =models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content = models.TextField(name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        db_table='comments'
        verbose_name='comment'
        verbose_name_plural='comments'    
    

