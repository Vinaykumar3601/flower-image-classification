import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

#load the trained model to classify the images

from keras.models import load_model
model = load_model('model1_flowers.h5')

#dictionary to label all the flower dataset classes.

classes = { 
    0:'daisy',
    1:'dandelion',
    2:'roses',
    3:'sunflowers',
    4:'tulips',
}
#initialise GUI

top=tk.Tk()
top.geometry('800x600')
top.title('Image Classification of flowers')
top.configure(background='#FFFFFF')
label=Label(top,background='#CDCDCD', font=('Ubuntu',18,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((180,180))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred=numpy.argmax(model.predict([image])[0])
    sign = classes[pred]
    print(sign)
    label.configure(background='white', foreground='#DC143C',font=('montserrat',18,'bold'), text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Check Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='white', foreground='#DC143C',font=('montserrat',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload new image",command=upload_image,padx=10,pady=5)
upload.configure(background='#DC143C', foreground='white',font=('montserrat',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Image Classification on flowers",pady=20, font=('montserrat',20,'bold'))
heading.configure(background='#DC143C',foreground='white')
heading.pack()
top.mainloop()