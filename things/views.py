from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, you can save the form
            form.save()
            # Redirect or indicate success after saving
    else:
        form = ThingForm()  # An unbound form

    return render(request, 'home.html', {'form': form})
