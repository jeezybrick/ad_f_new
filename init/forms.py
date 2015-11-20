from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import InlineField


class MyWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (
            forms.widgets.TextInput(attrs={'size': '4', 'placeholder': '###', 'maxlength': '3'}),
            forms.widgets.TextInput(attrs={'size': '4', 'placeholder': '###', 'maxlength': '3'}),
            forms.widgets.TextInput(attrs={'size': '6', 'placeholder': '####', 'maxlength': '4'}),
        )
        super(MyWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.mid, value.num]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return (
                '<div class="row phone-inputs">'
                '<div class="col-lg-12 col-xs-12">'
                '<div class="form-inline">'
                '<div class="col-md-3 col-xs-3 col-sm-3">%s</div>'
                '<div class="col-md-1 col-xs-1 col-sm-1 text-center">-</div>'
                '<div class="col-md-3 col-xs-3 col-sm-3">%s</div>'
                '<div class="col-md-1 col-xs-1 col-sm-1 text-center">-</div>'
                '<div class="col-md-3 col-xs-3 col-sm-3">%s</div>'
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
        return values[0] + values[1] + values[2]


class DemoForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = PhoneField(required=True, label='')
    url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'demo_form'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-md-7'

        self.helper.add_input(Submit('submit', 'Request demo',
                                     css_class='btn btn-default btn-md'))

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
                'url', placeholder='Website/URL (optional)'
            )
        )
