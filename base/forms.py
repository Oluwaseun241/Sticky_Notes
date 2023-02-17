from django.forms import ModelForm
from .models import StickyNote

class StickyNoteForm(ModelForm):
    class Meta:
        model = StickyNote
        fields = '__all__'