from django.shortcuts import render, redirect, get_object_or_404

from .forms import SupplementForm
from .models import Supplement

# Create your views here.


def index(request):
    queryset = Supplement.objects.all()
    context = {'supplements': queryset}
    return render(request, 'index.html', context=context)


def add(request):
    if request.method == 'POST':
        form = SupplementForm(request.POST, request.FILES)
        if form.is_valid():
            supplement = form.save(commit=False)
            image = form.cleaned_data['image']
            supplement.save()
            return redirect('index')

    context = {'form': SupplementForm()}
    return render(request, 'add.html', context=context)


def detailed_view(request, supplement_id):
    supplement = get_object_or_404(Supplement, pk=supplement_id)
    context = {'supplement': supplement}
    return render(request, 'detailed_view.html', context=context)




