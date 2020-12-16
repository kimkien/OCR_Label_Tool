import tkinter as tk
import glob
import matplotlib.pyplot as plt
import json
from PIL import Image
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
  label_fn = os.path.join(args.dataset, img_name.rsplit(".")[0] + '.json')
  if os.path.exists(label_fn):
    continue
  ls_json.append(label_fn)
  ls_img.append(os.path.join(args.dataset, img_name))

def show_img(image_id, canvas2):
  print(ls_img[idx])

  img0= Image.open(ls_img[idx])
  w,h= img0.size
  print(h)
  if (w>800):
    h_ = int((w/800)*h)
    print(h_)
    img0= img0.resize((800,h_))
  img_ = ImageTk.PhotoImage(img0)
  canvas2.img= img_0
  canvas2.itemconfigure(image_id, image=img_)

def nextImage(event=None):
  global idx, image_id, canvas2
  print(idx)
  print(ls_img)

  label = entry1.get()
  if len(label):
    with open(ls_json[idx], 'w',encoding='utf-8') as f:
      res = {"label": label, "path": ls_img[idx]}
      json.dump(res, f, ensure_ascii=False)   
      idx+=1
      if idx==len(ls_img):
        label3 = tk.Label(root, text='DONE!')
        label3.config(font=('helvetica', 30))
        canvas1.create_window(400, 140, window=label3)
        return
      entry1.delete(0, "end")
      # show_img(image_id, canvas2)
      img0 = Image.open(ls_img[idx])
      w,h= img0.size
      print(h)
      if (w>800):
        h_ = int((w/800)*h)
        print(h_)
        img0= img0.resize((800,h_))
      img_ = ImageTk.PhotoImage(img0)
      canvas2.img= img_
      canvas2.itemconfig(image_id, image=img_)

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 800, height = 200,  relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='OCR LABEL TOOL ')
label1.config(font=('helvetica', 14))
canvas1.create_window(400, 25, window=label1)

label2 = tk.Label(root, text='Value:')
label2.config(font=('helvetica', 13))
canvas1.create_window(400, 100, window=label2)

entry1 = tk.Entry(root, width=100) 
canvas1.create_window(400, 140, window=entry1)

root.bind('<Return>', nextImage)
button1 = tk.Button(text='Next', command=nextImage, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 180, window=button1)
    
canvas2 = tk.Canvas(root, width = 1000, height = 500,  relief = 'raised')
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


  
