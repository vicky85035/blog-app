from django.db import models
from django.conf import settings
# from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story_by = models.CharField(max_length=100,default='Member_only_story')
    title = models.CharField(max_length=250)
    thought = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    post_img = models.ImageField(upload_to='post_img/', null=True, blank=True)
    description = models.TextField()
    # tags = TaggableManager()

    class Meta:
        unique_together = ('title','thought','description')

    def __str__(self):
        return f'{self.title}, written by {self.user}'