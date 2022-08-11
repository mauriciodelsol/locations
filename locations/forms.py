from django import forms
from locations.models import Location

class LocationForm(forms.ModelForm):
    houmer_id = forms.IntegerField(required=True)
    lat = forms.DecimalField(min_value=-90, max_value=90, required=True)
    lon = forms.DecimalField(min_value=-90, max_value=90, required=True)
    speed = forms.IntegerField(min_value=0, required=True)

    class Meta:
        model = Location
        fields = ['houmer_id', 'lat', 'lon', 'speed']
