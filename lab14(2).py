print("Welcome to task 2!")
import json
with open("image_info_test-dev2017.json", "r") as f:
    data = json.load(f)
    
    image = data.get("images", [])
    images = len(image)
    print("Number of images: ",images)
    
    category = data.get("categories", [])
    categories = len(category)
    print("Number of categories: ", categories)

    if "images" in data:
        for image in data["images"]:
            file_name = image["file_name"]
            if file_name == "000000000001.jpg":
                coco_url = image.get("coco_url")
                height = image.get("height")
                width = image.get("width")
                id = image.get("id")
                print(f"Image URL: {coco_url}")
                print(f"Height: {height}")
                print(f"Width: {width}")
                print(f"ID: {id}")
    
    max_number = 0
    img = None
    for image in data["images"]:
        number = int(image["file_name"][:len(image["file_name"])-4])
        if number == 1:
            img = image
        if number > max_number:
            max_number = number
    max = ("0" * (12-len(str(max_number)))) + str(max_number) + ".jpg"
    print("The image with the highest number:", max)        
