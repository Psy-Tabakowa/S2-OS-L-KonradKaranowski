from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg


from frames.base_frame_results import BaseResultsFrame


class ResultFrameAlg1(BaseResultsFrame):

    def __init__(self, container, controller, names, times, previous, **kwargs):
        super().__init__(container, controller, **kwargs)

        # variables for times and names
        self.names = names
        self.times = times

        # store prevoious params
        self.previous = previous

        # params key
        self.params = 'alg1_params'

        # create title
        self.create_title('Access to processor simulation results')

        # create dummy canvas
        self.create_canvas()

    def create_canvas(self):
        figure = Figure(figsize=(3, 3), dpi=100)
        axis = figure.add_subplot(111)
        colors = ['red', 'blue', 'green', 'purple']
        axis.bar(self.names, self.times, color=colors)
        axis.grid()

        canvas = FigureCanvasTkAgg(figure=figure, master=self.container)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def execute(self):
        self.controller.execute_access_to_processor(*self.previous)
