import json

with open('image_info_test-dev2017.json') as jsonfile:
    data = json.load(jsonfile)
    count_images = len(data['images'])
    print(f'Number of pictures: {count_images}')
    
    count_cat = len(data['categories'])
    print(f'Number of categories: {count_cat}')
    
    images = data['images']
    max_num = 0
    
    for img in images:
        if img['file_name'] == '000000000001.jpg':
            print('Parametres of 000000000001.jpg:',
                  '-' * 30,
                  f'URL to the photo: {img['coco_url']}',
                  f'Height of the photo: {img['height']}',
                  f'Width of the photo: {img['width']}',
                  f'Identifier of the photo: {img['id']}',
                  '-' * 30,
                  sep = '\n'
            )
            
        if img['id'] > max_num:
            max_num = int(img['id'])
            max_images = img['file_name']
    
    print(f'Image with the highest number: {max_images}')