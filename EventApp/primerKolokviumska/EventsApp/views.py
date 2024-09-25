from django.shortcuts import render
from .models import Event, Band, BandEvent
from .forms import EventForm

# Create your views here.


def index(request):
    queryset = Event.objects.filter(kreator=request.user)
    context = {'events': queryset}
    return render(request, 'index.html', context=context)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            field1 = form.cleaned_data['field1']
            field2 = form.cleaned_data['field2']
            field3 = form.cleaned_data['field3']
            field4 = form.cleaned_data['field4']
            bands = field2.split(',')
            event = Event()
            event.kreator = request.user
            event.ime = field1
            event, create = Event.objects.get_or_create(event, ime=event.ime)
            bands = []
            for name in bands:
                band, created = Band.objects.get_or_create(name=name)
                bandEvent = BandEvent.objects.create(event=event, band=band)
                bands.append(band)

    form = EventForm()
    context = {'form': form}
    return render(request, 'master_add.html', context=context)