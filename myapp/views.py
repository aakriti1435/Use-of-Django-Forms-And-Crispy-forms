from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

# Create your views here.
def contact(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name,email) 


    form = ContactForm()
    return render(request, "form.html", {'form':form})
    #return HttpResponse("contact view")


def snippet_detail(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SnippetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #print('VALID')
            form.save()

    form = SnippetForm()
    return render(request, "form.html", {'form':form})
    #return HttpResponse("contact view")
