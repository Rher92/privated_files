from django import forms
from django.contrib.auth import get_user_model
from .models import Bucket, Files


User = get_user_model()


class FileFieldForm(forms.ModelForm):
    class Meta:
        model = Bucket
        fields = (
            "name",
            "files",
            "user"
        )

    name = forms.CharField(
        label='Name',
        required=True,
        max_length=255
    )
    user = forms.ModelChoiceField(
        label='User',
        required=True,
        queryset=User.objects.filter(),
    )
    files = forms.FileField(
        label='File',
        required=True,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    def save(self):
        files = self.files.getlist('files')
        bucket = super().save()
        for _file in files:
            instance = Files(
                files=_file,
                bucket=bucket
            )
            instance.save()