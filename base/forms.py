from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['note_text']

        widgets = {
            'note_text': forms.Textarea(attrs={'rows': 3}),
        }