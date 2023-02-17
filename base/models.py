from django.db import models

# Create your models here.
class StickyNote(models.Model):
    note_text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)