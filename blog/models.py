from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_image/', null=True, blank=True)
    short_description = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'created_by')

    def __str__(self):
        return f'{self.title}, written by {self.created_by}'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey("accounts.User", related_name="user_tags", on_delete=models.SET_NULL, null=True)

class PostTag(models.Model):
    tag = models.ForeignKey(Tag, related_name="post_tags", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="user_post_tags", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tag', 'post')