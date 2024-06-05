from django.db import models
from model_utils.models import TimeStampedModel
import uuid
from users.models import User

# Create your models here.
class Post(TimeStampedModel):
    
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    content = models.TextField(null=False, blank=True)
    published = models.BooleanField(default=False)
    # image = models.FileField(upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        
        db_table='posts'
        verbose_name='post'
        verbose_name_plural='posts'
        
    def __str__(self) -> str:
        return self.id
    
class Like(TimeStampedModel):
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts') 
    
    class Meta:
        db_table='likes'
        
    def __str__(self) -> str:
        return f'{self.user.username}-{self.post.title}'  
        