import requests

def get_wallpapers(name):
    
    url = f"https://wallhaven.cc/api/v1/search?categories={name}"
    try:
        response = requests.get(url)

        if(response.status_code == 200):
            data = response.json()
            wallpapers_urls =  get_urls(data)
            print(wallpapers_urls)
            return wallpapers_urls
        else:
            print("Error : " , response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Errro : " , e)
        return None

def get_urls(data):
    wallpaper_urls = []
    for image in data['data']:
        wallpaper_urls.append(image['path'])

   
    return wallpaper_urls

# def main():
#     tag = input("Enter a category : ")
#     get_wallpapers(tag)

# if __name__ == '__main__':
#     main()