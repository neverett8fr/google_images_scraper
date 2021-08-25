import requests, urllib

def all_img_urls(search_word, count):
    # this routine returns a list of all urls with images

    j = 0
    while j < count:
        r = requests.get(
            "https://www.google.com/search?q=" + search_word + "&tbm=isch" + "&num=1" + "&start=" + str(1*j) + "&safe=off")

        for i, val in enumerate(str(r.text.replace(">", "").split("<")).split()):
            if "src=\"http" in val:
                # output.append(val.replace("src=\"", "").replace("\"/',", ""))
                download_img_thumbnail_singular(val.replace("src=\"", "").replace("\"/',", ""), j)
        j += 1


def download_img_thumbnail_singular(url, number):
    try:
        with open("images/" + "img_" + number + ".jpg", "wb") as handle:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                handle.write(block)
    except:
        print("Error - Not found")


def download_img_thumbnails(url_array):

    for i, url in enumerate(url_array):
    #    # wb write binary
        try:
            with open("images/" + "img_" + str(i)+".jpg", "wb") as handle:
                r = requests.get(url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        except:
            print("Error - Not found")

        #try:
        #    urllib.request.urlretrieve(url, "images/img_"+str(i)+".jpeg")
        #except:
        #    print("Not found")




search_par = input("Enter the images you want to search for:  ").replace(" ", "%20")
search_num = input("Enter the amount of images you want:  ")
search_type = input("Enter thumbnail(0) or image(1):  ")
if search_type == "0":
    # download_img_thumbnails(all_img_urls(search_par, int(search_num)))
    download_img_thumbnail_singular(all_img_urls(search_par, int(search_num)))

#all_img_urls(search_par, int(search_num))