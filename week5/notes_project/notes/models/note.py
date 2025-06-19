from django.db import models
from django.conf import settings
from .folder import Folder

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # when a folder gets deleted, notes in it also get deleted.
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 'created_at' and 'updated_at' fields gets value automatically.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
