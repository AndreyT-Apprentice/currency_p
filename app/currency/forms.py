from currency.models import ContactUS, Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency_type',
            'sale',
            'buy',
            'source',
        )


class ContactUSForm(forms.ModelForm):

    class Meta:
        model = ContactUS
        fields = (
            "subject",
            "message",
            )


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = (
            "source_name",
            "source_url",
            )
