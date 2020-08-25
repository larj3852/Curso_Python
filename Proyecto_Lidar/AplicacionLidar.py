import tkinter as Tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
#%%

class Aplicacion():
    def __init__(self):
        self.tamano     = "700x500" #Columnasxfilas
        self.ventana    = Tk.Tk()
        self.ventana.wm_title("Tkinter+Matplotlib")
        self.ventana.iconbitmap("Proyecto_Lidar\Matlab.ico")
        self.ventana.geometry(self.tamano)
        self.Grafico()

    def lanzar(self):
        self.ventana.mainloop()
    
    
    def Grafico(self):
        """ Embebiendo Matplotlib graphic en Tkinter 
            Referencias:        https://matplotlib.org/3.1.1/gallery/mplot3d/subplot3d.html
                                https://matplotlib.org/3.1.1/gallery/mplot3d/scatter3d.html
                                #Manejo de excepciones con canvas 
                                https://matplotlib.org/3.3.1/users/event_handling.html
                                #Uso de mpl_toolkits.mplot3d --> Axes3D
                                https://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#subplotting
                                #Enable figure movement by mouse
                                https://stackoverflow.com/questions/8475235/how-to-enable-rotation-in-an-axes3d-matplotlib-embedded-in-a-pyqt4-widget
        """
        fig = Figure(figsize=(5, 4), dpi=100)           #DPI = Dots/inch figsize = Tamaño en pulgadas filxcol
        t = np.arange(0, 3, .01)
        #ax =fig.add_subplot(111,projection="3d")        #Atributo del objeto plot
        ax = Axes3D(fig)
        ax.plot([1,2,3],[1,2,3],[1,2,3])
        ax.plot(t,2 * np.sin(2 * np.pi * t),2 * np.cos(2 * np.pi * t))
        ax.scatter(0,0,0,marker=11)
        
        """ Creacion de figura en Canvas"""
        canvas = FigureCanvasTkAgg(fig, master=self.ventana)  # A tk.DrawingArea.
        ax.mouse_init()     #Este tiene que ir exclusivamente despues de declarar inicializar el canvas
        canvas.draw()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)    #Empaquetando la figura
        """ Creacion del toolbar """
        toolbar = NavigationToolbar2Tk(canvas, self.ventana)
        toolbar.update()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)   #Empaquetado del toolbar 

        """ Recepcion de eventos en caso de interacciones """
        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        canvas.mpl_connect("key_press_event", on_key_press)

        def _quit():
            self.ventana.quit()     # stops mainloop
            self.ventana.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        button = Tk.Button(self.ventana, text="Quit", command=_quit)
        button.pack(side=Tk.BOTTOM)



app = Aplicacion()
app.lanzar()
