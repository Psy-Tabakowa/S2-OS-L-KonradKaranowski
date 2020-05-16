import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


from ..base_frame_choose_params import BaseChooseParamsFrame


class ChooseFrameAlg3(BaseChooseParamsFrame):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, controller, **kwargs)

        # create variables
        self.num_of_pages = tk.IntVar(value=5)
        self.process_length = tk.IntVar(value=30)
        self.process_pages = tk.IntVar(value=7)

        # create title
        self.create_title('Page replacement simulation')
        # create entries
        self.create_entries()

    def create_entries(self):
        self.container.columnconfigure((0, 1), weight=1)
        num_of_pages_label = ttk.Label(
            self.container,
            text='Enter number of pages: '
        )
        num_of_pages_label.grid(row=0, column=0)
        num_of_pages_entry = tk.Entry(
            self.container,
            textvariable=self.num_of_pages,
            width=10
        )
        num_of_pages_entry.grid(row=1, column=0)

        length_process_label = ttk.Label(
            self.container,
            text='Enter number of pages for process:'
        )
        length_process_label.grid(row=0, column=1)
        length_process_entry = tk.Entry(
            self.container,
            textvariable=self.process_pages,
            width=10
        )
        length_process_entry.grid(row=1, column=1)

        length_process_label = ttk.Label(
            self.container,
            text='Enter length of process:'
        )
        length_process_label.grid(row=0, column=2)
        length_process_entry = tk.Entry(
            self.container,
            textvariable=self.process_length,
            width=10
        )
        length_process_entry.grid(row=1, column=2)

        # blank line
        blank = ttk.Label(self.container)
        blank.grid(row=3, column=0, columnspan=2, pady=40)

    def execute(self):
        if self.validate():
            self.controller.execute_page_replacement(
                self.num_of_pages.get(),
                self.process_pages.get(),
                self.process_length.get()
            )
        else:
            tkinter.messagebox.showinfo('Error', 'Enter correct values.')

    def validate(self):
        pages = self.num_of_pages.get()
        p_pages = self.process_pages.get()
        length = self.process_length.get()
        if type(pages) != int or pages <= 0:
            return False
        if type(p_pages) != int or p_pages <= pages:
            return False
        if type(length) != int or length <= 0:
            return False
        return True

    def show_summary(self):
        self.controller.show_frame('summary3')
