from django.shortcuts import render



def my_homepage_view(request):
    return render(request, 'main_page.html')
