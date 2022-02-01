from asyncio.windows_events import NULL
from textwrap import indent
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from django.template import context, loader

from taskApp.models import Sections, Books
from taskApp.serializers import SectionSerializer, BookSerializer
from django.core import serializers
import json

# Create your views here.

@csrf_exempt
def index(request):
    print(request)
    book = Sections.objects.all()
    context = {
        'book': book
    }
    return render(request, 'book/index.html', context)

def edit(request):
    sec = Sections.objects.get(SectionId=1)
    context = {
        'sec': sec
    }
    return render(request, 'sections/edit.html', context)

def show(request):
    sec = Sections.objects.all()
    context = {
        'sec': sec
    }
    return render(request, 'sections/show.html', context)

def add(request):
    return render(request, 'sections/add.html')
    

@csrf_exempt
def sectionApi(request, Id=0):

    if request.method == 'GET':
        section = Sections.objects.all()
        section_serializer = SectionSerializer(section, many=True)
        data = serializers.serialize('json', section_serializer)
        context = {
            'sec': section,
            'section_data': data
        }
        return render(request, 'sections/index.html', context)

    elif request.method == 'POST':
        print(request)
        section_data = JSONParser().parse(request)
        # section_serializer = SectionSerializer(data=section_data)
        
        # if section_serializer.is_valid():
        #     section_serializer.save()
        #     return JsonResponse('Added Successfully', safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        section_data = JSONParser().parse(request)
        print(section_data)
        section = Sections.objects.get(SectionId=section_data['SectionId'])
        section_serializer = SectionSerializer(section, data=section_data)

        if section_serializer.is_valid():
           section_serializer.save()
           book = Sections.objects.all()
           context = {
            'book': book
           }
           return render(request, 'book/index.html', context)
        
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        
        section = Sections.objects.get(SectionId=Id)
        section.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def bookApi(request, Id=0):

    if request.method == 'GET':

        book = Books.objects.all()
        book_serializer = BookSerializer(book, many=True)
        # print(section_serializer)
        return JsonResponse(book_serializer.data, safe=False)

    elif request.method == 'POST':

        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'DELETE':
        
        book = Books.objects.get(BookId=Id)
        book.delete()
        return JsonResponse("Deleted Successfully", safe=False)