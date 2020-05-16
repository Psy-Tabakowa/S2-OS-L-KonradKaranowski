import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class MainFrame(ttk.Frame):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller

        # container for title
        self.title_container = tk.Frame(self, bd=10, relief='groove')
        self.title_container.pack(side='top', fill='both', expand=True)
        # container for entries
        self.container = tk.Frame(self, bd=10, relief='groove')
        self.container.pack(side='top', fill='both', expand=True)
        # container for buttons
        self.button_container = tk.Frame(self, bd=10, relief='groove')
        self.button_container.pack(side='top', fill='x', expand=True)

        # place title
        self.title_place()
        # place image
        self.container_place()
        # create buttons
        self.create_buttons()

    def title_place(self):
        title = ttk.Label(
            self.title_container,
            text='Operating systems simulation manager',
            font=40
        )
        title.config(anchor='center')
        title.pack(side='top', fill='x', expand=True)

    def container_place(self):
        canvas = tk.Canvas(
            self.container,
            height=300,
            width=200
        )
        canvas.grid(row=0, column=0, sticky='nsew')
        img = Image.open('os.png')
        img.thumbnail((500, 400))
        canvas.image = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

    def create_buttons(self):
        self.button_container.columnconfigure((0, 1, 2), weight=1)
        button1 = ttk.Button(
            self.button_container,
            text='Access to processor'
        )
        button1.grid(row=4, column=0, sticky='ew')
        button1['command'] = lambda: self.controller.show_frame('alg1_params')

        button2 = ttk.Button(
            self.button_container,
            text='Access to disk'
        )
        button2.grid(row=4, column=1, sticky='ew')
        button2['command'] = lambda: self.controller.show_frame('alg2_params')

        button3 = ttk.Button(
            self.button_container,
            text='Page replacement'
        )
        button3.grid(row=4, column=2, sticky='ew')
        button3['command'] = lambda: self.controller.show_frame('alg3_params')
