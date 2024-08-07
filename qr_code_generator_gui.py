import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img_file = "generated_qr.png"
        img.save(img_file)

        img = Image.open(img_file)
        img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel.config(image=img)
        panel.image = img

        messagebox.showinfo("Success", f"QR code saved as {img_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the widgets
label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=20)

panel = tk.Label(root)
panel.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
