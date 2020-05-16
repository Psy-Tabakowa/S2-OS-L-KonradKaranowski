import tkinter as tk
from tkinter import ttk


from frames import MainFrame, \
    ChooseFrameAlg1, ResultFrameAlg1, SummaryAlg1, \
    ChooseFrameAlg2, ResultFrameAlg2, SummaryAlg2, \
    ChooseFrameAlg3, ResultFrameAlg3, SummaryAlg3
from components import execute_access_to_processor,\
    execute_access_to_disk, \
    execute_page_replecement


FRAMES = {
    'main_menu': MainFrame,
    'alg1_params': ChooseFrameAlg1,
    'alg2_params': ChooseFrameAlg2,
    'alg3_params': ChooseFrameAlg3,
    'summary1': SummaryAlg1,
    'summary2': SummaryAlg2,
    'summary3': SummaryAlg3
}


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.title("Operating Systems simulation manager")
        self.resizable(False, False)
        self.geometry("550x410")

        # main container
        self.container = ttk.Frame(self)
        self.container.grid()

        self.frames = dict()
        for key, frame in FRAMES.items():
            print(key)
            self.frames[key] = frame(self.container, controller=self)
            self.frames[key].grid(row=0, column=0, sticky='nsew')
        self.show_frame('main_menu')

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def execute_access_to_processor(self, num_of_processes, phase_len_min, phase_len_max):
        params = (num_of_processes, phase_len_min, phase_len_max)
        names, times = execute_access_to_processor(num_of_processes,
                                                   phase_len_min,
                                                   phase_len_max)
        self.frames['alg1_result'] = ResultFrameAlg1(self.container, self, names, times, params)
        self.frames['alg1_result'].grid(row=0, column=0, sticky='nsew')
        self.frames['alg1_result'].tkraise()

    def execute_access_to_disk(self, num_of_blocks, num_of_requests):
        params = (num_of_blocks, num_of_requests)
        queues, cylinders, names = execute_access_to_disk(num_of_blocks,
                                                          num_of_requests)
        self.frames['alg2_result'] = ResultFrameAlg2(self.container, self, queues,
                                                     cylinders, names, params)
        self.frames['alg2_result'].grid(row=0, column=0, sticky='nsew')
        self.frames['alg2_result'].tkraise()

    def execute_page_replacement(self, pages, p_pages, length):
        params = (pages, p_pages, length)
        deficiencies, names = execute_page_replecement(pages, length, p_pages)
        self.frames['alg3_result'] = ResultFrameAlg3(self.container, self, deficiencies, names, params)
        self.frames['alg3_result'].grid(row=0, column=0, sticky='nsew')
        self.frames['alg3_result'].tkraise()
