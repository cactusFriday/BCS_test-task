from django.shortcuts import render

# Create your views here.
def transaction(request):
    return render(request, template_name='index.html', context={})

def index(request):
    return render(request, template_name='tx_list.html', context = {})