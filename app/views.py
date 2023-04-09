from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.

def topicform(request):
    tfo=Topicform()
    d={'forms':tfo}
    if request.method=='POST':
        tf=Topicform(request.POST)
        if tf.is_valid():
            t=tf.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=t)[0]
            T.save()
            return HttpResponse('save successfully')
    return render(request,'topicform.html',d)

def student(request):
    sfo=Studentform()
    d={'form':sfo}
    if request.method=='POST':
        tf=Studentform(request.POST)
        if tf.is_valid():
            tf.save()
            return HttpResponse('save successfully')
    return render(request,'student.html',d)

def subjectform(request):
    sfo=Subjectform()
    d={'form':sfo}
    if request.method=='POST':
        sf=Subjectform(request.POST)
        if sf.is_valid():
            sf.save()
            return HttpResponse('successfully')
    return render(request,'subjectform.html',d)