from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name = tn)[0]
        TO.save()
        QLTO = Topic.objects.all()
        d = {'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO = Topic.objects.all()
    d1 = {'topic':QLTO}
    if request.method == 'POST':
        tn = request.POST['tn']
        na = request.POST['name']
        ur = request.POST['url']
        TO=Topic.objects.get(topic_name = tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        
        QLWO = Webpage.objects.all()
        d2 = {'webpages':QLWO}
        return render(request,'display_webpage.html',d2)
    return render(request,'insert_webpage.html',d1)

def insert_accessrecord(request):
    QLWO = Webpage.objects.all()
    d3 = {'webpages':QLWO}
    if request.method == 'POST':
        na = request.POST['na']
        da = request.POST['date']
        auth = request.POST['author']

        WO = Webpage.objects.get(pk = na)
        ARO = AccessRecord.objects.get_or_create(name = WO,date = da,author = auth)[0]
        ARO.save()

        QLAO = AccessRecord.objects.all()
        d4={'accessrecords':QLAO}
        return render(request,'display_accessrecord.html',d4)
    return render(request,'insert_accessrecord.html',d3)