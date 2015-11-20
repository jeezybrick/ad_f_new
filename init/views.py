from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from init import forms


# For login
class HomeView(View):
    form_class = forms.DemoForm
    template_name = 'home.html'
    title = _('Home')

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        context = {
            'form': form,
            'title': self.title,
        }
        if form.is_valid():
            return redirect(self.get_success_url())
        return TemplateResponse(request, self.template_name, context)

    def get_success_url(self):
        return reverse("thanks")


class ThanksView(View):
    template_name = 'thanks.html'
    title = _('Thank you')

    def get(self, request):
        print('than view')
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)