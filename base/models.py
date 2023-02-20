from django.db import models

# Create your models here.
class StickyNote(models.Model):
    note_text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    background_color = models.CharField(max_length=255, default='#FFFFFF')

    def __str__(self):
        return self.note_text