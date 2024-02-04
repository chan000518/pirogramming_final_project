from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .geocoding import *

# 골프장 목록 표시
def location_list(request):
    locations = GolfLocation.objects.all()
    ctx = {
        'locations' : locations
    }
    return render(request, 'locations/location_list.html', ctx)

#골프장 세부 내용 표시
def location_detail (request, pk):
    location = GolfLocation.objects.get(id=pk)
    ctx = {
        'location' : location,
        'pk' : pk
    }
    return render(request, 'locations/location_detail.html', ctx)


#새로운 골프장 추가
def location_create (request):
    if request.method == 'POST':
        form = NewField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('locations:list')
        
    else:
        form = NewField()
        ctx = {
            'form' : form
        }
        return render(request, 'locations/location_create.html', ctx)
    
#골프장 변경사항 수정
def location_update(request, pk):
    location = GolfLocation.objects.get(id=pk)
    if request.method == "POST":
        form = NewField(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
        return redirect('locations:detail', pk=pk)
    else:
        form = NewField(instance=location)
        ctx = {
            'location' : location, 
            'form' : form, 
            'pk' : pk,
        }
        return render(request, 'locations/location_update.html', ctx)
    
#골프장 삭제
def location_delete(request, pk):
    if request.method == 'POST':
        location = GolfLocation.objects.get(id=pk)
        location.delete()
        return redirect('locations:list')
    
def location_distance (request):
    address = "경기도 군포시 수리산로 244" #사용자 외래키에서 주소 필드 가져오기 {{user.address}}
    instances = GolfLocation.objects.all() #사용자 주소와 비교할 골프장 인스턴스들
    
    nearest = find_nearest_golf(address, instances)
    ctx = {
        'nearest' : nearest,
    }
    return render(request, 'locations/location_distance.html', ctx)