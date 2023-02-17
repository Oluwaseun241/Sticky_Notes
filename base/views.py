from django.shortcuts import render
from .models import StickyNote

# Create your views here.
def home(request):
    notes = StickyNote.objects.all()
    context = {'notes': notes}
    return render(request, 'base.html', context)

def create(request):
    if request.method == 'POST':
        note_text = request.POST['note_text']
        return redirect('home')
    return render(request, 'form.html')