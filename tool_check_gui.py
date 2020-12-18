import tkinter as tk
import json
import os
import argparse
import tkinter as tk
from PIL import ImageTk,Image  

 
idx=0
ls_img = []
ls_json= []
parser = argparse.ArgumentParser(description='Labeling tool for license plate OCR')
parser.add_argument('--dataset', type=str, required=True,
                        help='Path of dataset')
args = parser.parse_args()

for img_name in os.listdir(args.dataset):
  if img_name.rsplit(".")[-1] in ["json", "JSON"]:
    continue
  label_fn = os.path.join(args.dataset, img_name.rsplit(".")[0] + '.json')
  
  str_label= None
  path_img= None
  print(label_fn)
  with open(label_fn,"r",encoding='utf-8-sig') as f:
    structure = f.read()
    data=json.loads(structure)
    str_label= data["label"]
    path_img= data["path"].split("\\")[-1]
  with open(label_fn,"w",encoding='utf-8') as f:
    res = {"label": str_label, "path": path_img}
    json.dump(res, f, ensure_ascii=False)
  ls_json.append(str_label)
  ls_img.append(os.path.join(args.dataset, img_name))

def show_img(idx, image_id, canvas2):
  if idx==len(ls_img):
    print("DONE")
    label3 = tk.Label(root, text='DONE!')
    label3.config(font=('helvetica', 30))
    canvas1.create_window(400, 140, window=label3)
    return

  img0 = Image.open(ls_img[idx])
  w,h= img0.size
  if (w>800):
    h_ = int((w/800)*h)
    img0= img0.resize((800,h_))
  img_ = ImageTk.PhotoImage(img0)
  canvas2.img= img_
  canvas2.itemconfig(image_id, image=img_)
  name= ls_img[idx].split("\\")[-1]
  label1["text"]= f'{name}'
  label2["text"]= f'{ls_json[idx]}'


def nextImage(event=None):
  global idx, image_id, canvas2
  label = entry1.get()
  if len(label):
    json_file= ls_img[idx].split(".")[0]+".json"
    with open(json_file, 'w',encoding='utf-8') as f:
      res = {"label": label, "path": ls_img[idx]}
      ls_json[idx]= label
      json.dump(res, f, ensure_ascii=False)
      entry1.delete(0, "end")
      print("len(label)")
  idx+=1
  show_img(idx, image_id, canvas2)

def backImage():
  global idx, image_id, canvas2
  label = entry1.get()
  if len(label):
    json_file= ls_img[idx].split(".")[0]+".json"
    with open(json_file, 'w',encoding='utf-8') as f:
      res = {"label": label, "path": ls_img[idx]}
      ls_json[idx]= label
      json.dump(res, f, ensure_ascii=False)   
      entry1.delete(0, "end")
      print("len(label)")
  idx-=1
  show_img(idx, image_id, canvas2)

root= tk.Tk()
root.title('KimKien\'s tool ')


canvas1 = tk.Canvas(root, width = 800, height = 300,  relief = 'raised')
canvas1.pack()
label0 = tk.Label(root, text='CHECKING LABEL TOOL ')
label0.config(font=('helvetica', 30))
canvas1.create_window(400, 25, window=label0)

name= ls_img[idx].split("\\")[-1]
label1= tk.Label(root, text=f'name')
label1.config(font=('helvetica', 10))
canvas1.create_window(400, 25, window=label0)

entry1 = tk.Entry(root, width=100) 
canvas1.create_window(400, 140, window=entry1)

root.bind('<Return>', nextImage)
button1 = tk.Button(text='Next', command=nextImage, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(430, 180, window=button1)

button1 = tk.Button(text='Back', command=backImage, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(370, 180, window=button1)


label2 = tk.Label(root, text=f'{ls_json[idx]}')
label2.config(font=('helvetica', 26))
canvas1.create_window(400, 220, window=label2)
    
canvas2 = tk.Canvas(root, width = 1000, height = 400,  relief = 'raised')
canvas2.pack()
img0= Image.open(ls_img[idx])
w,h= img0.size
if (w>800):
  h_ = int((w/800)*h)
  img0= img0.resize((800,h_))

img = ImageTk.PhotoImage(img0)

image_id =canvas2.create_image(500,200, anchor="center", image=img)
# show_img()

root.mainloop()


  
