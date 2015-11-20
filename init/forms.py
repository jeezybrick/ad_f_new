from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class DemoForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'

        self.helper.add_input(Submit('submit', 'Request demo',
                                     css_class='btn btn-default btn-md'))

        self.helper.layout = Layout(
            Field(
                'first_name', placeholder='First name'
            ),
            Field(
                'last_name', placeholder='Last name'
            )
            ,
            Field(
                'email', placeholder='Email'
            )
            ,
            Field(
                'url', placeholder='Website/URL (optional)'
            )
        )
