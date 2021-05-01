from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Bucket(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        User,
        related_name="bucket",
        on_delete=models.CASCADE
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Files(models.Model):
    files = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    bucket = models.ForeignKey(
        Bucket,
        on_delete=models.SET_NULL,
        null=True,
        related_name="files",
    )

    def __str__(self):
        return f'{self.files.name}'