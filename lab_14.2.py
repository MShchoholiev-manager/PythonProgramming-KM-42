print('Welcome to lab 14 task 2.')

import json

def count(data):
    image_count = 0
    categorie_count = 0
    if 'images' in data:
        image_count = len(data['images'])
    else:
        print('Key "images" not found in the file.')

    if 'categories' in data:
        categorie_count = len(data['categories'])
    else:
        print('Key "categories" not found in the file.')

    print(f'In file there are {image_count} images and {categorie_count} categories.')

try: 
    with open('image_info_test-dev2017.json', 'r') as f:
        data = json.load(f)
        count(data)
except FileNotFoundError as e:
    print(e)

max_number = 0
img_0 = None

if 'images' in data:
    for image in data['images']:
        name = image['file_name']
        number = int(name[:len(name)-4])
        if number == 1:
            img_0 = image
        if number > max_number:
            max_number = number
            max_image_name = name

    search_filename = '000000000001.jpg'
    if 'images' in data:
        for image in data['images']:
            file_name = image['file_name']
            if file_name == search_filename:
                coco_url = image.get('coco_url', 'URL not found')
                height = image.get('height', 'Height not found')
                width = image.get('width', 'Width not found')
                image_id = image.get('id', 'ID not found')
                print(f'Image URL: {coco_url}')
                print(f'Height: {height}')
                print(f'Width: {width}')
                print(f'ID: {image_id}')
                break

    print(f'The image with the highest number is: {max_image_name}')

else:
    print('Key "images" not found in the file.')
