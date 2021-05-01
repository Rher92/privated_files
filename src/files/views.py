from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FileFieldForm
from .models import Files, Bucket
from django.views.generic import View
from django.views.generic.edit import FormView


def home(request):
    buckets = Bucket.objects.all()
    return render(request, "files/home.html", {"buckets": buckets})


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = "files/model_form_upload.html"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            bucket = form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse('home')

class ProtectFiles(View):
    def dispatch(self, request, *args, **kwargs):
        allow_request = False
        path = kwargs.get('path')
        if request.user.is_authenticated:
            allow_request = True
        if allow_request:
            response = HttpResponse()
            del response['Content-Type']
            response['X-Accel-Redirect'] = '/protected_media/' + path
            return response
        else:
            return HttpResponseForbidden('Not authorized to access this media.')    