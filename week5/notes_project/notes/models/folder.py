from django.db import models
from django.conf import settings

class Folder(models.Model):

    # Connects each folder to its owner(user)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Folder's display name
    name = models.CharField(max_length=100)

    # makes parent folder optional where parent is the foreign key of the same model.
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    # if parent folder gets deleted, child folders will get delete too.

    # Automatically sets when folder was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns folder's name
        return self.name