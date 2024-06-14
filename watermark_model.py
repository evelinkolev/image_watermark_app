from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarking App")
        self.window.geometry("600x400")

        self.image_label = Label()
        self.image_label.pack()

        self.image_upload_btn = Button(text="Upload Image", command=self.upload_image)
        self.image_upload_btn.pack()

        self.watermark_entry = Entry()
        self.watermark_entry.pack()

        self.add_watermark_btn = Button(text="Add Watermark", command=self.add_watermark)
        self.add_watermark_btn.pack()

        self.image_save_btn = Button(text="Save Image", command=self.save_image)
        self.image_save_btn.pack()

        self.image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path) if file_path else None
        self.display_image(self.image)

    def display_image(self, image):
        if image:
            img_display = ImageTk.PhotoImage(image.resize((400, 300)))
            self.image_label.config(image=img_display)
            self.image_label.image = img_display

    def add_watermark(self):
        text = self.watermark_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter a watermark text")
            return
        self.watermarked_image = self.image.copy() if self.image else None
        if self.watermarked_image:
            draw = ImageDraw.Draw(self.watermarked_image)
            font = ImageFont.load_default()
            width, height = self.watermarked_image.size
            draw.text((width - 100, height - 30), text, font=font, fill="white")
            self.display_image(self.watermarked_image)

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            self.watermarked_image.save(file_path) if file_path else None
        else:
            messagebox.showerror("Error", "No watermarked image to save")

    def run(self):
        self.window.mainloop()
