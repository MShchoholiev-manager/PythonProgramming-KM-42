


import re


pose_estimation = "[BodyPart:1-(0.51, 0.28) score=0.82 BodyPart:2-(0.60, 0.29) score=0.82 BodyPart:3-(0.62, 0.38) score=0.84 BodyPart:4-(0.60, 0.30) score=0.10 BodyPart:5-(0.42, 0.29) score=0.72 BodyPart:6-(0.38, 0.39) score=0.81 BodyPart:8-(0.55, 0.49) score=0.53 BodyPart:9-(0.68, 0.64) score=0.84 BodyPart:10-(0.59, 0.80) score=0.67 BodyPart:11-(0.44, 0.50) score=0.51 BodyPart:12-(0.29, 0.64) score=0.80 BodyPart:13-(0.37, 0.81) score=0.76 BodyPart:16-(0.55, 0.18) score=0.81 BodyPart:17-(0.47, 0.18) score=0.91]"



points = str(re.findall(r'BodyPart:\d+-\(([^,]+), ([^)]+)\)', pose_estimation))
new_points = points.replace("(", "")
scores = re.findall(r'score=([0-9.]+)', pose_estimation)
print("points =", new_points.replace(")", ""))
print("scores =", scores)



