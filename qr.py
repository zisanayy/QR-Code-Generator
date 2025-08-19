import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode
import png
from tkinter import colorchooser



def create_qr_code():
    url = url_entry.get().strip()  

    if not url:
        status_label.config(text="Please enter a valid URL!")
        return

    qr_url = pyqrcode.create(url)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".svg",
            filetypes=[("SVG Files", "*.svg"), 
               ("PNG Files", "*.png")]
    )

    qr_color = getattr(application_window, "qr_color", "#000000")  
    
    if file_path.endswith(".svg"):
        with open(file_path, "wb") as f:
            qr_url.svg(f, scale=8, module_color=qr_color)
        status_label.config(text="QR Code has been created and saved!")
    elif file_path.endswith(".png"):
        qr_url.png(file_path, scale=8, module_color=qr_color)
        status_label.config(text="QR Code has been created and saved!")


    
def choose_color():
 color_code = colorchooser.askcolor(title="Choose QR Code Color")
 if color_code[1]:
     color_label.config(text=color_code[1])
     application_window.qr_color = color_code[1]
 


application_window=tk.Tk()  
application_window.title("QR Code Generator")

label=tk.Label(application_window,text="URL Enter:")
url_entry=tk.Entry(application_window,width=40)
qr_button=tk.Button(application_window,text="Create QR Code",command=create_qr_code)
status_label=tk.Label(application_window,text="")
color_button = tk.Button(application_window, text="Choose QR Color", command=choose_color)
color_label = tk.Label(application_window, text="#000000")

label.grid(row=0,column=0,padx=10,pady=10)
url_entry.grid(row=0,column=1,padx=10,pady=10)
qr_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
status_label.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
color_button.grid(row=3, column=0, padx=10, pady=10)
color_label.grid(row=3, column=1, padx=10, pady=10)






application_window.mainloop()