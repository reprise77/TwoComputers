import socket
import sys
from tkinter import *
from PIL import Image, ImageTk
import threading


class ImageServerApp:
    def __init__(self):
        self.root = Tk()

        self.root.title("Image Viewer")
        self.current_image_index = 0
        self.image_paths = [f"Images\\{i}.jpg" for i in range(1, 12)]
        image = Image.open(self.image_paths[self.current_image_index])
        self.photo = ImageTk.PhotoImage(image)
        self.label = Label(self.root, image=self.photo)
        self.label.pack()
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.daemon = True
        self.server_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.root.quit()
        sys.exit()

    def change_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_paths):
            self.current_image_index = 0
        new_image = Image.open(self.image_paths[self.current_image_index])
        new_photo = ImageTk.PhotoImage(new_image)

        self.label.configure(image=new_photo)
        self.label.image = new_photo
        self.photo = new_photo

    def run_server(self):
        server_ip = "0.0.0.0"
        server_port = 3000
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)

        while True:
            client_socket, client_address = server_socket.accept()
            self.change_image()
    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ImageServerApp()
    app.start()