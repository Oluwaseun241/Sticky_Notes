from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote

# Create your views here.
def home(request):
    notes = StickyNote.objects.all()
    context = {'notes': notes}
    return render(request, 'base.html', context)

def create(request):
    context = {}
    if request.method == 'POST':
        note_text = request.POST['note_text']
        note = StickyNote.objects.create(note_text=note_text)
        context = {'note': note}
        return redirect('home')
    
    return render(request, 'form.html', context)

def delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('home')

def update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == 'POST':
        note_text = request.POST.get('note_text')
        note.note_text = note_text
        note.save()
        return redirect('home')

    context = {'note': note}
    return render(request, 'update.html', context)