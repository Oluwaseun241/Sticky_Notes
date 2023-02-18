from django.forms import ModelForm, Textarea
from django import forms
from .models import StickyNote

class StickyNoteForm(ModelForm):
    class Meta:
        model = StickyNote
        fields = '__all__'