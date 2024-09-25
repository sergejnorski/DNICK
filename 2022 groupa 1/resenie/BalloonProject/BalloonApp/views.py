from django.shortcuts import render, redirect, get_object_or_404

from BalloonApp.forms import FlightForm
from BalloonApp.models import Flight


# Create your views here.


# Со користење на Bootstrap рамката креирајте 2 темплејти за приказ на информациите
# од системот. Соодветно:
# - /index/ - приказ на општи информации за системот, прикажано на Слика1
def index(request):
    return render(request, 'index.html')


# /flights/ - приказ на сите летови кои се креирани од најавениот корисник и
# полетуваат од аеродром Скопје. Во овој приказ дополнително се наоѓа и форма
# за додавање на нов лет, прикажано на Слика2
def flights(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.creator = request.user
            image = form.cleaned_data['image']
            flight.save()
            return redirect('flights')

    queryset = Flight.objects.filter(creator=request.user).filter(airport_from='Skopje')
    context = {'flights': queryset, 'form': FlightForm}
    return render(request, 'flights.html', context=context)


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flights')
    else:
        form = FlightForm(instance=flight)

    context = {'form': form}
    return render(request, 'edit_flight.html', context=context)


def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == 'POST':
        flight.delete()
        return redirect('flights')

    return render(request, 'delete_flight.html')
