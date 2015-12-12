from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from init import forms, utils


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
            utils.send_email_with_form_data(request.POST)
            return redirect(self.get_success_url())
        return TemplateResponse(request, self.template_name, context)
        # return redirect('/#demo_form')

    def get_success_url(self):
        return reverse("thanks")


class ThanksView(View):
    template_name = 'thanks.html'
    title = _('Thank you')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class PolicyView(View):
    template_name = 'policy.html'
    title = _('Policy')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class TermsView(View):
    template_name = 'terms.html'
    title = _('Terms')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class FaqView(View):
    template_name = 'faq.html'
    title = _('FAQ')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class PolicyTwoView(View):
    template_name = 'policy_two.html'
    title = _('Policy')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class TermsTwoView(View):
    template_name = 'terms_two.html'
    title = _('Terms')

    def get(self, request):
        context = {
            'title': self.title,
        }
        return TemplateResponse(request, self.template_name, context)


class JoinNetworkView(View):
    template_name = 'join_network.html'
    title = _('Join network')
    form_class = forms.JoinNetworkForm

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
            #utils.send_email_with_form_data(request.POST)
            return redirect(self.get_success_url())
        return TemplateResponse(request, self.template_name, context)
        # return redirect('/#demo_form')

    def get_success_url(self):
        return reverse("home")
