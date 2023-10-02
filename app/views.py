from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import shortuuid
from .models import *
import datetime
import json
from .utils import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    print(request.user)
    return render(request, 'home.html')


def create_shorturl(request):

    if request.method == "POST":
        data = json.loads(request.body)
        orignal_url = data.get('orignal_url')
        short_url = shortuuid.uuid()[:6]
        base_url = request.build_absolute_uri("/")
        short_uri = f"{base_url}s/{short_url}"

        
        if request.user.is_authenticated:
            exist = Shorten_url.objects.filter(orignal_url=orignal_url,creator=request.user)
            if exist.exists():
                return JsonResponse({"message": "URL already Exist", "short_url": ""})
            
            expire = datetime.datetime.now() + datetime.timedelta(days=365)
            Shorten_url.objects.create(
                orignal_url=orignal_url, short_url=short_url, creator=request.user, expries_date=expire)

            return JsonResponse({"message": "Short Url Created Successfully", "short_url": short_uri})
        else:
            expire = datetime.datetime.now() + datetime.timedelta(days=30)
            Shorten_url.objects.create(
                orignal_url=orignal_url, short_url=short_url, expries_date=expire)
            return JsonResponse({"message": "If you want to Track & Save \
                             your short url please login or singup.", "short_url": short_uri})
    return HttpResponse("Unauthrize",status=404)


def redirect_real_url(request, short_url):
    url = Shorten_url.objects.filter(short_url=short_url)

    if url.exists():
        url_obj = url.first()
        client_ip = get_ip(request)
        location = get_location_from_ip(client_ip)
        Clicks_short_url.objects.create(short_url=url_obj,location=location)

        return redirect(url_obj.orignal_url)
    
    return HttpResponse("URL not found",status=404)

@login_required
def profile(request):
    short_urls = Shorten_url.objects.filter(creator=request.user.id).order_by("-created_at")
    clicks = []
    for url_obj in short_urls:
        click = Clicks_short_url.objects.filter(short_url=url_obj).count()
        clicks.append(click)
    data = zip(short_urls,clicks)
    return render(request,"profile.html",{"data":data})

def delete_short_url(request,id):
    Shorten_url.objects.get(id=id).delete()
    return redirect("profile")


def get_url_deatils(request):
    d = json.loads(request.body)
    id =  d.get("id")
    data = {}
    url = Shorten_url.objects.filter(id=id).first()

    data["orignal_url"] = url.orignal_url
    data["short_url"] = f"http://127.0.0.1:8000/s/{url.short_url}"
    data["created"] = url.created_at
    data["exprie"] = url.expries_date
    all_clicks = Clicks_short_url.objects.filter(short_url=url).values()

    data["clicks"] =  list(all_clicks)

    return JsonResponse(data)    