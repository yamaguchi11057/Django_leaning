import logging
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import InquiryForm

logger = logging.getLogger(__name__)

# Create your views here.
class ToBuyList(TemplateView):
    template_name = 'index.html'

class InquiryView(FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('tobuyapp:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'The message has been sent')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
        