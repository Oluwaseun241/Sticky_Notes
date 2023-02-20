from django.forms import ModelForm, Textarea
from django import forms
from .models import StickyNote
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FieldWithButtons

class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = '__all__'

        widgets = {
            'note_text': forms.Textarea(attrs={'rows': 5, 'style': 'font-size: 16px' 'font-family: sans-serif'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'style': 'width: 100px'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'note_text',
            Submit('submit', 'Save'),
        )