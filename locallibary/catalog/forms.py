from django                     import forms
from django.core.exceptions     import ValidationError
from django.utils.translation   import gettext_lazy as _
import datetime

class RenewItemForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if its inn the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is after 4 weeks.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        #clean data.
        return data
