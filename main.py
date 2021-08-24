

import requests

def all_img_urls(search_word, count):
    # this routine returns a list of all urls with images

    output = []

    j = 0
    while j < count:
        r = requests.get(
            "https://www.google.com/search?q=" + search_word + "&tbm=isch" + "&num=3" + "&start=" + str(3*j))

        for i, val in enumerate(str(r.text.replace(">", "").split("<")).split()):
            if "src=\"http" in val:
                output.append(val.replace("src=\"", "").replace("\"/',", ""))
                # print(val.replace("src=\"", "").replace("\"/',", ""))
        j += 3

    return output

def download_img(url_array):

    for i, url in enumerate(url_array):
        # wb write binary
        with open("images/" + str(i)+".jpg", "wb") as handle:
            r = requests.get(url, stream=True)

            for block in r.iter_content(1024):
                if not block:
                    break

                handle.write(block)

search_par = input("Enter the images you want to search for:  ")
search_num = input("Enter the amount of images you want:  ")

download_img(all_img_urls(search_par, int(search_num)))