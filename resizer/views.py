from django.http import Http404
from django.urls import reverse
from django.views import generic

from . import models, forms


class ImageListView(generic.ListView):
    model = models.ModifiedImage
    template_name = 'resizer/image_list.html'
    paginate_by = 50


class ImageDetailView(generic.DetailView):
    model = models.ModifiedImage
    template_name = 'resizer/image_detail.html'


class ImageCreateView(generic.FormView):
    form_class = forms.DownloadImageForm
    template_name = 'resizer/image_create.html'

    def form_valid(self, form):
        instance = form.save()
        self.success_url = reverse('image_resize', kwargs=dict(pk=instance.pk))
        return super().form_valid(form)


class ImageResizeView(generic.CreateView):
    form_class = forms.ResizeImageModelForm
    template_name = 'resizer/image_resize.html'

    def get_form_kwargs(self):
        try:
            obj = models.SourceImage.objects.get(pk=self.kwargs['pk'])
        except models.SourceImage.DoesNotExist:
            raise Http404
        form_kwargs = super().get_form_kwargs()
        form_kwargs['source_image'] = obj
        return form_kwargs



