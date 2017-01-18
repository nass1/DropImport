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
    try:
        for i in imageslist1:
            print count, ":  ", i
            count += 1
            if "jpg_640x640.jpg" in i or "jpeg_640x640.jpeg" in i:
                for a in imageslist1[count-2:count-1]:
                    mainImages.append(a)
    except:
        mainImages = None
    return mainImages

def ImgeFiltersSelection(imageslist):
    selectionImages = []
    count = 1
    imageslist1 = Imageclean(imageslist)
    try:
        for i in imageslist1:
            print count, ":  ", i
            count += 1
            if "jpg_640x640.jpg" in i or "jpeg_640x640.jpeg" in i:
                for a in imageslist1[count-2:count-1]:
                    for b in imageslist1[:count-2]:
                        selectionImages.append(b)
    except:
        selectionImages = None
    return selectionImages



def ImgeFiltersOther(imageslist):
    otherImages = []
    count = 1
    imageslist1 = Imageclean(imageslist)
    try:
        for i in imageslist1:
            print count, ":  ", i
            count += 1
            if "jpg_640x640.jpg" in i or "jpeg_640x640.jpeg" in i:
                for c in imageslist1[count-1:]:
                    otherImages.append(c)
    except:
        otherImages = None
    return otherImages