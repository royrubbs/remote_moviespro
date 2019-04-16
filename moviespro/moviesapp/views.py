from django.shortcuts import render
from .models import TeluguMovieApp
from .forms import TeluguMovieForm
from django.http.response import HttpResponse

def homeview(request):
    return render(request,'homeview.html')

def teluguview(request):
    return render(request,'teluguview.html')


def hindiview(request):
    return render(request,'hindiview.html')

def englishview(request):
    return render(request,'englishview.html')

def booknowview(request):
    if request.method=="POST":
        form=TeluguMovieForm(request.POST)
        if form.is_valid():
            Director_name=request.POST.get('Director_name','')
            Hero_name=request.POST.get('Hero_name','')
            Heroin_name=request.POST.get('Heroin_name','')
            Producer_name=request.POST.get('Producer_name','')
            Release_dt=request.POST.get('Release_dt','')
            data=TeluguMovieApp(
                Director_name=Director_name,
                Hero_name=Hero_name,
                Heroin_name=Heroin_name,
                Producer_name=Producer_name,
                Release_dt=Release_dt
            )
            data.save()
            form=TeluguMovieForm()
            return render(request,'booknowview.html',{'form':form})
    else:
        form=TeluguMovieForm()
        return render(request,'booknowview.html',{'form':form})




def telugudata(req):
    data=TeluguData.objects.all()
    return render((req,'telugudata.html',{'data':data}))
