from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .forms import SearchForm, GetCommentForm
import shopify
from .otherFunction import ImgeFilters, ImgeFiltersSelection, ImgeFiltersOther
import re
#___________________________________________________________________________________
api = "d8abe2f7be6107b6f6f4cc5f220f14ca"
password = "73f30d24102f182b6cb7b1b4e9b8b6f1"
shared_secret = "0b4c643fa7edd739a1dda92bade84e22"
url_format = "https://apikey:password@hostname/admin/resource.json"
shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
shopify.ShopifyResource.set_site(shop_url)
key = "DA8gz8DqfsXnYcm8iH54zM9x_zRynBRw_IJAnL8Xszw."
#___________________________________________________________________________________



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
                soup = BeautifulSoup(data, "html.parser")
                images = [] #The Images
                
                for i in soup.find_all("img"):
                    if "https" in i.get("src"):
                        c = i.get("src")
                        images.append(c)
                images1 =  ImgeFilters(images)
                images2 =  ImgeFiltersSelection(images)
                images3 =  ImgeFiltersOther(images)
                #print "========Images========"
                #print images1
                
                title =  soup.title.text #Title

                #print "the Size are are ______________________________________________>"
                Size = []  #The size
                for i in soup.findAll("a", {"data-role": "sku"}):
                    if len(i.text) != 0:
                        #print i.text, "=====>", len(i.text), "======>", type(len(i.text))
                        Size.append(i.text)


                # "the Discrption are are ______________________________________________>"
                Discrption = []
                for i in soup.findAll("li",{"class":"property-item"}):
                    #print i.text
                    Discrption.append(i.text)

                # "the Price is/are ______________________________________________>"
                price = None
                for i in soup.findAll("span", {"class": "p-price"}):
                    price = i.text
                    break;
                
                print "this is suppose to be comments"
                #---------------------------------------------------------
                
                for link in soup.find_all('iframe'):
                    abc = link.get('thesrc')
                    abc1 = "http:%s" % (abc)
                print (abc1)
                
                r1 = requests.get(abc1)
                
                data1 = r1.text
                
                soup1 = BeautifulSoup(data1, "html.parser")
     
                count = 0
                comments = []
                for link in soup1.find_all("dt", {"class": "buyer-feedback"}):
                    count += 1
                    print ("-----------Comment %s --------------" % (count))
                    print (link.text)
                    comments.append(link.text)

    
                context = {
                           "title": title,
                           "size": Size,
                           "price": price,
                           "images1": images1,
                           "images2": images2, 
                           "images3": images3,  
                           "form": form,
                           "Discrption":Discrption,
                           "comments": comments,

                           }
                return render(request, 'suppliers1.html', context)
            except:
                return render(request, 'suppliers1.html', {'error': 'error'})
    else:
        form = SearchForm()
    return render(request, 'suppliers1.html', {'form': form})








def postAli(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    new_product = shopify.Product()
    shop = shopify.Shop.current()
    if request.method == 'POST':
        q = request.POST['title']
        dis = request.POST['dis']
        priceAli = request.POST['price']
        priceFinal = re.sub(r'-.*$',"",priceAli)
        mainPic = request.POST.getlist('checksMain[]')
        #q = request.POST['title']
       
        #new product: title, discrption
        new_product.title = q
        new_product.body_html = dis
        #new_product.add_variant = 
        new_product.save()
    
        print ">>>>>>>>>>>>", shop.id
     
        # Main Image:
        imgID = [None]
        for i in mainPic:
            new_image = shopify.Image()
            new_image = shopify.Image(dict(product_id=new_product.id))
            new_image.src = i
            new_image.save()
            imgID.append(new_image.id)
            
        print "imagei",">>>>>", imgID[1]
        print priceFinal
        #Variants
        productvar = shopify.Product.find(new_product.id)
        
        variant2 = shopify.Variant(dict(price=float(priceFinal), option1="first", image_id=imgID[1]))    
        variant3 = shopify.Variant(dict(price=float(priceFinal), option1="third"))
        productvar.variants = [variant2, variant3]  
        productvar.save()
        
        #Price

        
    else:
        return HttpResponseRedirect("/AliExpress/")

    return HttpResponseRedirect("/AliExpress/")
        
    