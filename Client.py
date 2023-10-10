import socket
from tkinter import *
from tkinter import font


def click_button():
    server_ip = "192.168.241.138"
    server_port = 3000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))


window = Tk()
window.title("Button")
window.geometry("800x600")
button_font = font.Font(size=30)
button = Button(text='PRESS', command=click_button, height=10, width=20, bg='Red', fg='White', font=button_font).place(
    x=200,
    y=190, width=400, height=200)
window.mainloop()
