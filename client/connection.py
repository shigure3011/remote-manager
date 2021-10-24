from typing import Sized

from numpy.random import bit_generator
from my_client import Client
from tkinter import font, ttk
from my_entry import MyEntry

IO_PORT = 5656


class Connection:
    def __init__(self, client, client_io, parent, UI_control):
        self.UI_control = UI_control
        self.client = client
        self.client_io = client_io
        self.parent = parent
        self.ip_entry = MyEntry(
            self.parent, 'Enter host ip', '', justify='center', font=("Segoe Ui", 13),
        )
        self.connect_button = ttk.Button(parent,
                                         text='Connect',
                                         style='Accent.TButton',
                                         command=self.connect_button_click)
        self.connect_button.bind("<Return>", self.handle_enter)
        self.ip_entry.bind("<Return>", self.handle_enter)
        self.connect_button.focus()

    def handle_enter(self, _):
        self.connect_button_click()

    def connect_button_click(self):
        server_ip = self.ip_entry.get()
        print(server_ip)
        if server_ip == '':
            server_ip = 'localhost'
        try:
            self.client.connect(server_ip)
            self.client_io.connect((server_ip, IO_PORT))
            self.UI_control.connect_accepted_handle()
            return True
        except Exception as e:
            print(e)
            self.UI_control.connect_failed_handle()
            return False
