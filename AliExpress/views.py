from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .forms import SearchForm

def helloAli(request):

    return render(request,"suppliers1.html")


def GetAli(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = cd['Search']
            try:
                r = requests.get(url)
                data = r.content
                soup = BeautifulSoup(r.content, "html.parser")
                images = [] #The Images
                print "the Imgaes are ______________________________________________>"
                for i in soup.find_all("img"):
                    if "https" in i.get("src"):
                        if "_50x50.jpg" in i.get("src"):
                            a = i.get("src").replace("_50x50.jpg", "")
                            images.append(a)
                        else:
                            b = i.get("src").replace("_50x50.jpeg", "")
                            images.append(b)
                print images
                print "the Title are are ______________________________________________>"
                title =  soup.title.text #Title

                print "the Size are are ______________________________________________>"
                Size = []  #The size
                for i in soup.findAll("a", {"data-role": "sku"}):
                    if len(i.text) != 0:
                        print i.text, "=====>", len(i.text), "======>", type(len(i.text))
                        Size.append(i.text)


                print "the Discrption are are ______________________________________________>"
                Discrption = []
                for i in soup.findAll("li",{"class":"property-item"}):
                    print i.text
                    Discrption.append(i.text)

                print "the Price is/are ______________________________________________>"
                price = None
                for i in soup.findAll("span", {"class": "p-price"}):
                    price = i.text
                    break;

                context = {
                           "title": title,
                           "size": Size,
                           "price": price,
                           "images": images,
                           "form": form,
                           "Discrption":Discrption,

                           }
                return render(request, 'suppliers1.html', context)
            except:
                return render(request, 'suppliers1.html', {'error': 'error'})
    else:
        form = SearchForm()
    return render(request, 'suppliers1.html', {'form': form})