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
            print(value)
            #return [value.day, value.month, value.year]
            return ''.join(value)
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return (
                '<div class="row phone-inputs">'
                '<div class="col-lg-12">'
                '<div class="form-inline">'
                '<div class="col-md-3 col-xs-3 col-sm-10">%s</div>'
                '<div class="col-md-1 col-xs-3 col-sm-10 text-center">-</div>'
                '<div class="col-md-3 col-xs-3 col-sm-2">%s</div>'
                '<div class="col-md-1 col-xs-3 col-sm-2 text-center">-</div>'
                '<div class="col-md-3 col-xs-4 col-sm-2">%s</div>'
                '</div>'
                '</div>'
                '</div>'
               ) % tuple(rendered_widgets)
        # return ''.join(rendered_widgets)


class DemoForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(required=False, widget=MyWidget, label='')
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
