import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm
from django.utils import timezone

# Create your views here.
def home(request):
    notes = StickyNote.objects.all()
    context = {'notes': notes}
    return render(request, 'base.html', context)

def create(request):
    form = StickyNoteForm()
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            color = f"hsl({random.randint(0, 360)}, {random.randint(50, 100)}%, {random.randint(70, 90)}%)"
            note.color = color
            note.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'form.html', context)

def delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('home')

def update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    form = StickyNoteForm(request.POST or None, instance=note)
    if form.is_valid():
        note = form.save(commit=False)
        note.last_updated = timezone.now()
        note.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'update.html', context)