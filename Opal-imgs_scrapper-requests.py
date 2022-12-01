import requests

def download_image(image_url: str, image_name: str):
    img_data = requests.get(image_url).content
    with open(image_name +";"+ opal['price']['formatted']+'.jpg', 'wb') as handler:
        handler.write(img_data)

for page in range(0,168,2):
        url = f"https://www.koroit-opal-company.com/api/v2/products?sort=position-asc&resultsPerPage=84&page={page}&categoryId=551DDBD9-8AD4-229C-164A-C0A82AB9D825&locale=en_GB&shop=80300026"
        response = requests.get(url)
        for opal in response.json()['products']:
            img_link = 'https://www.koroit-opal-company.com' + opal['image']['url']
            print(opal['name'], opal['price']['formatted'], img_link)
            download_image(img_link, opal['name'])




