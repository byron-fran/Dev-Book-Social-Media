from django.db import models
from model_utils.models import TimeStampedModel
import uuid
from users.models import User
from .managers import PostManager
from ckeditor.fields import RichTextField, CKEditorWidget

# Create your models here.
class Post(TimeStampedModel):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    content = RichTextField(name="content")
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    objects = PostManager()

    class Meta:
        db_table = "posts"
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self) -> str:
        return f"{self.content[:20]}"

class Like(TimeStampedModel):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        db_table = "likes"

    def __str__(self) -> str:
        return f"{self.user.username}"


class Saved(TimeStampedModel):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="saved")

    class Meta:
        db_table = "saved"

    def __str__(self) -> str:
        return f"{self.user.username}"
