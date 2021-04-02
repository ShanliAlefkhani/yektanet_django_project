from django.shortcuts import render
from advertiser_management.models import Advertiser, Ad
from django.shortcuts import redirect


def index(request):
    advertisers = Advertiser.objects.all()
    context = {'advertisers': advertisers}
    return render(request, 'ads.html', context)


def detail(request, object_id):
    return redirect(Ad.objects.get(id=object_id).link)