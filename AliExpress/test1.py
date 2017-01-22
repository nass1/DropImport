from bs4 import BeautifulSoup
import requests
"""
url = "https://www.aliexpress.com/item/Upgrade-Waterproof-Digital-DSLR-Photo-Padded-Backpack-Multi-functional-SLR-Camera-Soft-Bag-Video-Case-for/32726032964.html?spm=2114.01010108.3.8.s13guz&ws_ab_test=searchweb0_0,searchweb201602_1_10065_10068_10000009_10084_10000025_10083_10080_10000029_10082_10081_10000028_10110_10111_10060_10112_10113_10062_10114_10056_10055_10037_10054_10059_10032_10099_10078_10079_10000022_10077_10000012_10103_10073_10102_10000015_10096_10000018_10000019_10052_10053_10107_10050_10106_10051,searchweb201603_10,afswitch_5,single_sort_2_default&btsid=28c4b134-c6ed-4f31-8a6d-ad594b6c2082"
r  = requests.get(url)
data = r.content
soup = BeautifulSoup(r.content, "html.parser")

print "the Imgaes are ______________________________________________>"
images1 = []
for i in soup.find_all("img"):
    if "https" in i.get("src"):
        c = i.get("src")
        images1.append(c)
print images1
#print images1[1:3]


print "=============================================>>>>>>>>>>>>>>>>>>>>>>>"
print "Here is the Function"
print "=============================================>>>>>>>>>>>>>>>>>>>>>>>"

def Imageclean(cleanlist):
    images = []
    for i in cleanlist:
        if "https" in i:
            if "_50x50.jpg" in i:
                a = i.replace("_50x50.jpg", "")
                images.append(a)
            else:
                b = i.replace("_50x50.jpeg", "")
                images.append(b)
    return images  



def ImgeFilters(imageslist):
    mainImages = []
    selectionImages = []
    otherImages = []
    count = 1
    imageslist1 = Imageclean(imageslist)
    for i in imageslist1:
        print count, ":  ", i
        count += 1
        if "jpg_640x640.jpg" in i or "jpeg_640x640.jpeg" in i:
            for a in imageslist1[count-2:count-1]:
                mainImages.append(a)

            for b in imageslist1[:count-2]:
                selectionImages.append(b)
            for c in imageslist1[count-1:]:
                otherImages.append(c)

    print "Main Images: ", len(mainImages)

    print "Selected Images: ", len(selectionImages)
    print "Selected Images: ", len(otherImages)
    print mainImages
    print "================================================================"
    print "================================================================"
    print selectionImages
    print "================================================================"
    print "================================================================"
    print otherImages
    return i

 

print "Clean____________________________________Clean"

abc = ImgeFilters(images1)

print abc


"""


'''
print "the Title are are ______________________________________________>"
print soup.title.text

print "the Size are are ______________________________________________>"
ab = []
for i in soup.findAll("a", {"data-role":"sku"}):
    if len(i.text) != 0 :
        print i.text , "=====>", len(i.text), "======>", type(len(i.text))
        ab.append(i.text)
print len(ab)

print "the Discrption are are ______________________________________________>"

for i in soup.findAll("li",{"class":"property-item"}):
    abc = type(i.text)
    print abc

print "the Price is/are ______________________________________________>"
for i in soup.findAll("span", {"class":"p-price"}):
    print i.text
    break;

    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    product.variants[0].price = price
        product.variants[0].option1 = "Pink"
        product.variants[0].option2 = "Red"
        product.variants[0].sku = "3245"
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
api = "d8abe2f7be6107b6f6f4cc5f220f14ca"
password = "73f30d24102f182b6cb7b1b4e9b8b6f1"
shared_secret = "0b4c643fa7edd739a1dda92bade84e22"
url_format = "https://apikey:password@hostname/admin/resource.json"
shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
#shopify.ShopifyResource.set_site(shop_url)
key = "DA8gz8DqfsXnYcm8iH54zM9x_zRynBRw_IJAnL8Xszw."
import json
import requests

request = requests.Session(auth=("d8abe2f7be6107b6f6f4cc5f220f14ca", "73f30d24102f182b6cb7b1b4e9b8b6f1"))
print json.loads(request.get('http://mr-nice.myshopify.com/admin/assets.json').content)



