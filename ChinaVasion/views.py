from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import SearchForm
import shopify
import requests
import json
#___________________________________________________________________________________
api = "d8abe2f7be6107b6f6f4cc5f220f14ca"
password = "73f30d24102f182b6cb7b1b4e9b8b6f1"
shared_secret = "0b4c643fa7edd739a1dda92bade84e22"
url_format = "https://apikey:password@hostname/admin/resource.json"
shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
shopify.ShopifyResource.set_site(shop_url)
key = "DA8gz8DqfsXnYcm8iH54zM9x_zRynBRw_IJAnL8Xszw."
#___________________________________________________________________________________
def hello(request):

    return render(request,"index.html")

#this function to search and retirve the information from ChinaVasion
def supp(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    if request.method == 'POST':
        form = SearchForm(request.POST)


        if form.is_valid():
            cd = form.cleaned_data
            codeFinal = cd['Search']
            getProductDetails_dic = {
                "key": key,
                "model_code": codeFinal,
            }
            try:
                r = requests.post(url, json=getProductDetails_dic)
                json_r = r.text
                json_load = json.loads(json_r)

                for i in json_load["products"]:
                    product_id_lst = i["product_id"]
                    product_name_lst = i["short_product_name"]
                    product_url_lst = i["product_url"]
                    product_price = i["price"]
                    category_name_lst = i["category_name"]
                    overview_lst = i["overview"]
                    main_picture_lst = i["main_picture"]
                    additional_images_lst = i["additional_images"]
                    #print (additional_images_lst)


                context = {"product_id_lst": str(product_id_lst),
                           "product_url_lst": product_url_lst,
                           "product_name_lst": product_name_lst,
                           "category_name_lst": category_name_lst,
                           "overview_lst": overview_lst,
                           "main_picture_lst": main_picture_lst,
                           "additional_images_lst": additional_images_lst,
                           "product_price": product_price,
                           "form": form,

                           }
                return render(request, 'suppliers.html', context)
            except:
                return render(request, 'suppliers.html', {'error': 'error'})
    else:
        form = SearchForm()
    return render(request, 'suppliers.html', {'form': form})





def PostToShpify(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    new_product = shopify.Product()
    if request.method == 'POST':
        q = request.POST['ProductName']
        dis = request.POST['dis']
        price = request.POST['price']
        mainPic = request.POST['mainPic']
        productType = request.POST['productType']

        additionalPic = request.POST.getlist('checks[]')
        print additionalPic


        new_product.title = q
        new_product.body_html = dis
        new_product.product_type = productType
        new_product.save()

        #Price
        product = shopify.Product.find(new_product.id)
        product.variants[0].price = price
        product.save()

        #Main Image
        new_image = shopify.Image()
        new_image = shopify.Image(dict(product_id=new_product.id))
        new_image.src = mainPic
        new_image.save()



        #additinola images
        #makelist1 = makelist.replace("[","").replace("u'","").replace("]","").replace(",","").replace("'","")
        for i in additionalPic:
            new_image = shopify.Image()
            new_image = shopify.Image(dict(product_id=new_product.id))
            new_image.src = i
            print i
            new_image.save()

            #print type(additionalPic)
            #print ("======>>>>>>>>>>", makelist1)
    else:
        return HttpResponseRedirect("/ChinaVasion/supp/")

    return HttpResponseRedirect("/ChinaVasion/supp/")