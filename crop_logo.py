import os
import argparse
import cv2
import json
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",help="path to logo directory")
parser.add_argument("-o","--output", help="path to directory store the crop image")
args = vars(parser.parse_args())

if not os.path.exists(args["output"]):
	os.mkdir(args["output"])

logo = os.listdir(args["input"])
for obj in logo:
	if obj.endswith("json"):
		continue
	else:
		base_name = os.path.splitext(obj)[0]
		ext = os.path.split(obj)[1]
		image = cv2.imread(os.path.join(args["input"],obj))
		json_file = base_name+".json"
		f = open(os.path.join(args["input"],json_file))
		data = json.load(f)
		h = data["imageHeight"]
		w = data["imageWidth"]
		for i in range(len(data["shapes"])):
			if data["shapes"][i]["label"] == "marker":
				points = data["shapes"][i]["points"]
				x_coor = []
				y_coor = []

				for j in range(len(points)):
				    x_coor.append(int(points[j][0]))
				    y_coor.append(int(points[j][1]))
				x_coor = np.asanyarray(x_coor)
				y_coor = np.asanyarray(y_coor)

				xmin = max(min(x_coor),0)
				ymin = max(min(y_coor),0)

				xmax = min(max(x_coor),w)
				ymax = min(max(y_coor),h)

				logo_crop = image[ymin:ymax, xmin:xmax]
				cv2.imwrite(os.path.join(args["output"],base_name+str(i)+".jpg"),logo_crop)



