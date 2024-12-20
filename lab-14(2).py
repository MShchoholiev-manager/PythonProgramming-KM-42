import json

file_path = 'image_info_test-dev2017.json'
with open(file_path, 'r') as file:
    data = json.load(file)

images_count = len(data['images'])

categories_count = len(data['categories'])

image_1 = next(image for image in data['images'] if image['id'] == 1)
coco_url = image_1['coco_url']
height = image_1['height']
width = image_1['width']
image_id = image_1['id']

max_image = max(data['images'], key=lambda x: x['id'])
max_image_name = max_image['file_name']

print(f"Number of photos: {images_count}")
print(f"Number of categories: {categories_count}")
print(f"Photo URL 000000000001.jpg: {coco_url}")
print(f"Height: {height}, Width: {width}, ID: {image_id}")
print(f"The name of the photo with the highest number: {max_image_name}")