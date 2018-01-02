import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import pandas as pd
import matplotlib.pyplot as plt

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.garden.matplotlib.backend_kivy import FigureCanvas


class MonApp(App):

    def build(self):
        self.df = pd.read_csv('./iris.csv')
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1)
        self.ax.hist(self.df['SepalLength'])
        # main
        self.root = BoxLayout()
        self.valuebox = BoxLayout()
        self.selectbox = BoxLayout()
        self.maincanvas = BoxLayout()
        self.root.add_widget(self.valuebox)
        self.root.add_widget(self.selectbox)
        self.root.add_widget(self.maincanvas)
        self.kaributton = Button(text='kari')
        self.valuebox.add_widget(self.kaributton)
        self.kari2button = Button(text='kari2')
        self.kari2button.bind(on_press=self.reloadcanvas)
        self.selectbox.add_widget(self.kari2button)
        self.maincanvas.add_widget(self.fig.canvas)
        return self.root

    def reloadcanvas(self, instance):
        self.ax.clear()
        self.ax.hist(self.df['SepalWidth'])
        self.fig.canvas.draw_idle()


if __name__ == '__main__':
    MonApp().run()
