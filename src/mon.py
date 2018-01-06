from pathlib import Path

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt
import pandas as pd

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView


class MonApp(App):

    def build(self):
        self.df = None
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1)
        # main
        self.root = BoxLayout(orientation='vertical')
        self.menubar = BoxLayout(size_hint_y=0.1)
        self.mainwindow = BoxLayout()
        self.valuescroll = ScrollView(size_hint_x=0.3)
        self.valuebox = BoxLayout(orientation='vertical')
        self.valuescroll.add_widget(self.valuebox)
        self.selectbox = BoxLayout(size_hint_x=0.3)
        self.maincanvas = BoxLayout()
        self.root.add_widget(self.menubar)
        self.root.add_widget(self.mainwindow)
        self.mainwindow.add_widget(self.valuescroll)
        self.mainwindow.add_widget(self.selectbox)
        self.mainwindow.add_widget(self.maincanvas)
        self.kaributton = Button(text='kari')
        self.valuebox.add_widget(self.kaributton)
        self.kaributton.bind(on_press=self.roadbutton)
        self.kari2button = Button(text='save')
        self.kari2button.bind(on_press=self.savecanvas)
        self.selectbox.add_widget(self.kari2button)
        self.maincanvas.add_widget(self.fig.canvas)

        # actionbar
        self.resourcebutton = Button(text='LoadResource')
        self.menubar.add_widget(self.resourcebutton)
        self.resourcebutton.bind(on_press=self.openpopup)

        # loadresource
        self.popup = Popup(title='Select Resource')
        self.popup_selectresource = BoxLayout(orientation='vertical')
        self.popup.add_widget(self.popup_selectresource)
        self.popup_button_csv = FileChooserListView()
        self.popup_close = Button(text='Close', on_press=self.get_file, size_hint_y=0.05)
        self.popup_selectresource.add_widget(self.popup_button_csv)
        self.popup_selectresource.add_widget(self.popup_close)

        return self.root

    def reloadcanvas(self, instance):
        self.ax.clear()
        self.ax.hist(self.df[instance.text])
        self.fig.canvas.draw_idle()

    def roadbutton(self, instance):
        self.valuebox.clear_widgets()
        for column in self.df.columns:
            self.valuebox.add_widget(Button(text=column, on_press=self.reloadcanvas))
            self.targetcolumn = column

    def savecanvas(self, instance):
        self.fig.canvas.print_png('XXXX.png')

    def openpopup(self, instance):
        self.popup.open()

    def get_file(self, instance):
        self.df = pd.read_csv(Path(str(self.popup_button_csv.selection[0])))
        self.popup.dismiss()


if __name__ == '__main__':
    MonApp().run()
