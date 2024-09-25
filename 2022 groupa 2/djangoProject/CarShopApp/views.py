from django.shortcuts import render, redirect, get_object_or_404

from .forms import FixForm
from .models import Fix

# Create your views here.


def index(request):
    return render(request, 'index.html')


def repairs(request):
    if request.method == "POST":
        form = FixForm(request.POST, request.FILES)
        if form.is_valid():
            fix = form.save(commit=False)
            fix.car_owner = request.user
            image = form.cleaned_data['image']
            fix.save()
            return redirect('repairs')

    queryset = Fix.objects.filter(car_owner=request.user, car__type='Sedan')
    context = {'cars': queryset, 'form': FixForm}
    return render(request, 'repairs.html', context=context)


def edit_fix(request, fix_id):
    fix = get_object_or_404(Fix, pk=fix_id)
    if request.method == "POST":
        form = FixForm(request.POST, request.FILES, instance=fix)
        if form.is_valid():
            form.save()
            return redirect('repairs')
    else:
        form = FixForm(instance=fix)
    context = {'form': form}
    return render(request, 'edit_fix.html', context=context)


def delete_fix(request, fix_id):
    fix = get_object_or_404(Fix, pk=fix_id)
    if request.method == "POST":
        fix.delete()
        return redirect('repairs')
    context = {'fix': fix}
    return render(request, 'delete_fix.html', context=context)
