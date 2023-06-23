import requests
import re
import os

user = input("Enter the image name: ")

user_agent = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

url = f"https://www.google.com/search?q={user}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjfx7KyqebuAhUQOSsKHc17DsEQ_AUoAXoECBgQAw&biw=1536&bih=760"

response = requests.get(url = url , headers = user_agent).text

pattern = "\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"

images = re.findall(pattern , response)

print(f"Total Images : {len(images)}")
no_of_images = int(input("Number of images to be downloaded: "))


if images:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)

    else:
        os.chdir(user)

    for image in images[:no_of_images]:
        image_url = eval(image)[0]
        response = requests.get(url = image_url).content
        image_name = image_url.split('/')[-1]

        with open(image_name , "wb") as file:
            file.write(response)



#["https://imageproxy.themaven.net//https%3A%2F%2Fwww.history.com%2F.image%2FMTYyNzgxMzA3MDcwMzI2MzYw%2Fmoon-gettyimages-490413228-promo.jpg",1080,1920]