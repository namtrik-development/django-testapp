from django import forms
from .models import Poll, Choice

class PollForm(forms.ModelForm):
  class Meta:
    model = Poll
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    """constructor que corrige error de validación de usuario. https://stackoverflow.com/q/51948640"""
    super().__init__(*args, **kwargs)
    self.fields['owner'].queryset = self.fields['owner'].queryset.distinct()

class ChoiceForm(forms.ModelForm):
  class Meta:
    model = Choice
    fields = '__all__'
