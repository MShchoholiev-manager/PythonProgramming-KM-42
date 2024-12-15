import json

with open("image_info_test-dev2017.json", "r") as file:
    data = json.load(file)

    num_images = len(data["images"])
    num_categories = len(data["categories"])
    photo_info = next(img for img in data["images"] if img["file_name"] == "000000000001.jpg")
    max_num_image = max(data["images"], key=lambda img: int(img["file_name"].split(".")[0]))

print("Number of images:", num_images)
print("Number of categories:", num_categories)
print("coco_url for 000000000001.jpg:", photo_info["coco_url"])
print("Height:", photo_info["height"])
print("Width:", photo_info["width"])
print("ID:", photo_info["id"])
print("Image with the highest number:", max_num_image["file_name"])