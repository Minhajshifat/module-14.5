from django import forms
from django.forms.widgets import NumberInput

class contactForm(forms.Form):
	name = forms.CharField()
	comment = forms.CharField(widget=forms.Textarea,required=False)
	email = forms.EmailField()
	accept=forms.BooleanField()
	birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	value = forms.DecimalField()
	FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
	favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
	colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)