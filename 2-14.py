import json

name = "image_info_test-dev2017.json"

with open(name) as file:
    
    dict = json.load(file)
    
    print(f' Кількість "images" у файлі "{name}": {len(dict["images"])}')

    print(f' Кількість "categories" у файлі "{name}": {len(dict["categories"])}')

    print("-"*50)

    for elem in dict["images"]:
        search = "000000000001.jpg"

        if elem["file_name"] == search:
            print (f' Для картинки "{search}":\n{" "*5}url: {elem["coco_url"]}\n{" "*5}height: {elem["height"]} \n{" "*5}width: {elem["width"]} \n{" "*5}id: {elem["id"]}')

    elem_list = []

    for elem in dict["images"]:
        
        elem_list.append(elem["file_name"])

    elem_list.sort(reverse=True)
    
    print(f"{"-"*50}\n Найбільша картинка за назвою: {elem_list[0]}")

