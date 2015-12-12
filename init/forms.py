import re
from django import forms
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class DemoForm(forms.Form):
    first_name = forms.CharField(label='')
    last_name = forms.CharField(label='')
    email = forms.EmailField(label='', required=True)
    phone = forms.CharField(required=True, label='',
                               validators=[
                                   validators.RegexValidator(r'^\d{3}\-\d{3}\-\d{4}$',
                                                             'Invalid phone format!',
                                                             'invalid'), ])
    company = forms.CharField(required=False, label='')
    url = forms.URLField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'demo_form'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-4 col-lg-offset-4 col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2 col-xs-10 col-xs-offset-1'
        self.form_show_errors = True
        self.helper.error_text_inline = True
        self.helper.help_text_inline = False
        self.helper.html5_required = True

        self.helper.add_input(Submit('submit', _('Request access'),
                                     css_class='form-button'))

        self.helper.layout = Layout(

            Field(
                'first_name',
                placeholder=_('First name')
            ),
            Field(
                'last_name',
                placeholder=_('Last name')
            )
            ,
            Field(
                'email',
                placeholder=_('Email')
            )

            ,
            Field(
                'phone',
                placeholder=_('###-###-####')
            )
            ,
            Field(
                'company',
                placeholder=_('Company name (optional)')
            )

            ,
            Field(
                'url',
                placeholder=_('http://www.yourwebsite.com (optional)')
            )
        )


class JoinNetworkForm(forms.Form):
    email = forms.EmailField(label='', required=True)
    phone = forms.CharField(required=True, label='',
                               validators=[
                                   validators.RegexValidator(r'^\d{3}\-\d{3}\-\d{4}$',
                                                             'Invalid phone format!',
                                                             'invalid'), ]
                            , help_text="<hr>")
    url = forms.URLField(label='', required=True, help_text="Don't worry, you can add more than one website later if you want!")
    website = forms.CharField(label='', required=True)
    accept = forms.BooleanField(label='', required=True, help_text="I accept the Terms & Conditions and Privacy Policy.")

    def __init__(self, *args, **kwargs):
        super(JoinNetworkForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'join_network_form'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-8 col-lg-offset-1 col-md-8 col-md-offset-1 col-sm-8 col-sm-offset-2 col-xs-10 col-xs-offset-1'
        self.form_show_errors = True
        self.helper.error_text_inline = True
        self.helper.help_text_inline = False
        self.helper.html5_required = True

        self.helper.add_input(Submit('submit', _('ACCESS NETWORK'),
                                     css_class='form-button'))

        self.helper.layout = Layout(

            Field(
                'website',
                placeholder=_('Website Name: e.g. Mommy on the Run')
            )
            ,
            Field(
                'url',
                placeholder=_('Website URL e.g. http://')
            ),

            Field(
                'phone',
                placeholder=_('###-###-#### (primary contact number)')
            )
            ,

            Field(
                'email',
                placeholder=_('Email (this will be your login/username)')
            )

            ,

            Field(
                'accept',
                placeholder=_('')
            )

        )
