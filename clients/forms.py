from django import forms
from django.forms import BooleanField

from clients.models import Newsletter, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('date_started', 'date_finished', 'periodicity', 'status', 'message', 'clients',)


class NewsletterManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('status',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'