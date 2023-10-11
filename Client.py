import socket
from tkinter import *
from tkinter import font
from tkinter.simpledialog import askstring


def get_server_ip():
    ip = askstring("IP Address", "Enter the server IP address:")
    if ip:
        return ip
        exit()


server_ip = get_server_ip()


def click_button():
    if server_ip:
        server_port = 3000

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))


window = Tk()
window.title("Button")
window.geometry("800x600")

button_font = font.Font(family='Helvetica', size=30)

button = Button(text='PRESS', command=click_button, height=10, width=20, bg='gray', fg='White', font=button_font)
button.place(x=200, y=190, width=400, height=200)

window.mainloop()
