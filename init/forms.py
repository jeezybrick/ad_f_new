import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import InlineField


class MyWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (
            forms.widgets.TextInput(attrs={'size': '4', 'placeholder': '###', 'pattern': '.{3}'}),
            forms.widgets.TextInput(attrs={'size': '4', 'placeholder': '###', 'pattern': '.{3}'}),
            forms.widgets.TextInput(attrs={'size': '6', 'placeholder': '####', 'pattern': '.{4}'}),
        )
        super(MyWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return (
                   '<div class="row phone-inputs">'
                   '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-10">'
                   '<div class="form-inline">'
                   '<div class="col-md-3 col-xs-3 col-sm-3">%s</div>'
                   '<div class="col-md-1 col-xs-1 col-sm-1 text-center">-</div>'
                   '<div class="col-md-3 col-xs-3 col-sm-3">%s</div>'
                   '<div class="col-md-1 col-xs-1 col-sm-1 text-center">-</div>'
                   '<div class="col-md-4 col-xs-4 col-sm-3">%s</div>'
                   '</div>'
                   '</div>'
                   '</div>'
               ) % tuple(rendered_widgets)


class PhoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(),
                       forms.CharField(),
                       forms.CharField()
                       ]
        super(PhoneField, self).__init__(list_fields, widget=MyWidget, *args, **kwargs)

    def compress(self, values):
        return ''.join(values)

    def clean(self, values):
        value = ''.join(values)
        reg = re.compile('\d{10}$')
        if not reg.match(value):
            raise ValidationError(_('Invalid phone format'))


class DemoForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)
    phone = PhoneField(required=True, label='')
    url = forms.URLField(label=_('Website/URL (optional)'), required=False)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.initial['phone'] = ['647', '328', '8001']

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'demo_form'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-md-7'
        self.form_show_errors = True
        self.helper.error_text_inline = True
        self.helper.help_text_inline = False
        self.helper.html5_required = True

        self.helper.add_input(Submit('submit', 'Request demo',
                                     css_class='jump-to-form-button'))

        self.helper.layout = Layout(

            InlineField(
                'first_name'
            ),
            InlineField(
                'last_name'
            )
            ,
            InlineField(
                'email'
            )
            ,
            Div(
                InlineField(
                    'phone'
                ), css_class='form-inline'
            )
            ,
            InlineField(
                'url'
            )
        )
