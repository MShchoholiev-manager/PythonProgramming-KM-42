import re
while(True):
    pose_estimation = str(input("Enter the points that were recognized by the system: "))
    regular_expression = re.compile(r'\(([\d.]+),\s*([\d.]+)\)\s*\w+=([\d.]+)')
    list_of_result = re.findall(regular_expression, pose_estimation)#data extracted by regular expression
    points = []
    scores = []
    for num in list_of_result:#create lists
        x, y, score = num
        points.extend([float(x), float(y)])
        scores.append(float(score))
    if (len(points) > 36) or (len(scores) > 18):#check the accuracy of the input
        print('Oops...Your data is inaccurate/unable to be used')
        continue
    else:
        print('points = ',points, '\n',
              'scores = ',scores,sep=''
        )
        break