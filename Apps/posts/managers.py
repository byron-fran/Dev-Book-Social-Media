from django.db.models import Manager

class PostManager(Manager):
    
    def list_posts(self):
        return self.all().order_by('-created')
    
    