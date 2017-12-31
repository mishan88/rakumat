import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import pandas as pd
import matplotlib.pyplot as plt

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas

fig, ax = plt.subplots(nrows=1, ncols=1)
df = pd.read_csv('./iris.csv')
ax.hist(df['SepalLength'])

canvas = fig.canvas


def callback(instance):
    canvas.draw()


class MatplotlibApp(App):
    title = 'MatplotlibApp'

    def build(self):
        bl = BoxLayout(orientation='vertical')
        a = Button(text='pressme')
        a.bind(on_press=callback)
        bl.add_widget(canvas)
        bl.add_widget(a)
        return bl


if __name__ == '__main__':
    MatplotlibApp().run()
