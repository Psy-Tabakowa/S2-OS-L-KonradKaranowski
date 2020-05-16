from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg
from tkinter import ttk


from frames.base_frame_results import BaseResultsFrame


class ResultFrameAlg3(BaseResultsFrame):

    def __init__(self, container, controller, deficiencies, names, previous, **kwargs):
        super().__init__(container, controller, **kwargs)

        # variables for times and names
        self.names = names
        self.deficiencies = deficiencies

        # store prevoious params
        self.previous = previous

        # params key
        self.params = 'alg3_params'

        # create title
        self.create_title('Page replacement simulation results')

        # create dummy canvas
        self.create_canvas()

    def create_canvas(self):
        figure = Figure(figsize=(3, 3), dpi=100)
        axis = figure.add_subplot(111)
        colors = ['red', 'blue', 'green', 'purple', 'green']
        bar_heights = [len(dfn) for dfn in self.deficiencies]
        axis.bar(self.names, height=bar_heights, color=colors)
        axis.grid()

        canvas = FigureCanvasTkAgg(figure=figure, master=self.container)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def execute(self):
        self.controller.execute_page_replacement(*self.previous)
