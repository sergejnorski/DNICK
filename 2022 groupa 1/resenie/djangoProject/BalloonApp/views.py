from django.shortcuts import render, redirect

from BalloonApp.forms import FlightForm
from BalloonApp.models import Flight
from django.shortcuts import get_object_or_404


# Create your views here.
def flights(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            photo = form.cleaned_data['photo']
            flight.save()
            return redirect('flights')

    queryset = Flight.objects.filter(user=request.user, airportFrom='Skopje').all()
    context = {'flights': queryset, 'form': FlightForm}
    return render(request, 'flights.html', context=context)


def index(request):
    return render(request, 'index.html')


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id, user=request.user)

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
    flight = get_object_or_404(Flight, id=flight_id, user=request.user)

    if request.method == 'POST':
        flight.delete()
        return redirect('flights')

    return render(request, 'delete_flight.html')
