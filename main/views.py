from django.http import HttpResponse
from django.shortcuts import render, redirect
from googletrans import Translator

# Create your views here.
from .forms import ImageForm
def home(request):
    return render(request, 'home.html')
def capturePage(request):
    return render(request, 'capturePage.html')
def uploadPage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request,'uploadPage.html',{'form': form,'img_obj': img_obj})
        else:
            form = ImageForm()
    else:
        form =ImageForm()
    return render(request, 'uploadPage.html', {'form': form})
def translated(request):
    txt = request.GET.get('text')
    lang = request.GET.get('lang')
    translator = Translator()
    out = translator.translate(txt, dest=lang)
    if (out == txt):
        return render(request, 'translated.html', {'translated': 'Invalid Text'})
    return render(request, 'translated.html', {'translated': out.text})
