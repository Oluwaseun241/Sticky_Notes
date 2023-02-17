from django.shortcuts import render
from .models import StickyNote

# Create your views here.
def home(request):
    notes = StickyNote.objects.get(id=1)
    context = {'notes': notes}
    return render(request, 'base.html', context)