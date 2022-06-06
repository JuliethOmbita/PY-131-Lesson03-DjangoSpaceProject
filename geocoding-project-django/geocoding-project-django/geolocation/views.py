from django.shortcuts import render
from .forms import AddressForm
from .utils import get_coordinates


# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            addy = form.cleaned_data['address']
            res = get_coordinates(addy)
            return render(request, 'geolocation/results.html', res)
    else:
    	form = AddressForm()
    return render(request, 'geolocation/index.html', {'form': form})