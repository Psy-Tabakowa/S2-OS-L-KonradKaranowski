import tkinter as tk
from tkinter import ttk
import abc


from frames.scrollable_frame import ScrollableFrame


class BaseSummary(ttk.Frame, abc.ABC):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller

        # container for title
        self.title_container = tk.Frame(self, bd=10, relief='groove')
        self.title_container.pack(side='top', fill='both', expand=True)
        # container for entries
        self.container = ScrollableFrame(self, bd=10, relief='groove')
        self.container.pack(side='top', fill='both', expand=True)
        # container for buttons
        self.button_container = tk.Frame(self, bd=10, relief='groove')
        self.button_container.pack(side='top', fill='x', expand=True)

    def title_place(self, text):
        title = ttk.Label(
            self.title_container,
            text=text,
            font=40
        )
        title.config(anchor='center')
        title.pack(side='top', fill='x', expand=True)

    def container_place(self, text):
        self.container.frame.columnconfigure(0, weight=1)
        label = ttk.Label(
            self.container.frame,
            text=text
        )
        label.grid(row=0, column=0, sticky='nsew')

    def create_buttons(self, place):
        self.button_container.columnconfigure(0, weight=1)
        button1 = ttk.Button(
            self.button_container,
            text='Back'
        )
        button1.grid(row=0, column=0, sticky='ew')
        button1['command'] = lambda: self.controller.show_frame(place)