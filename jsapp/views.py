from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'jsapp/base.html')

def day1(request):
    return render(request, 'jsapp/day1.html')


def day2(request):
    return render(request, 'jsapp/day2.html')

def day3(request):
    return render(request, 'jsapp/day3.html')

def day4(request):
    return render(request, 'jsapp/day4.html')