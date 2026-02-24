from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
import threading
import subprocess

# تصميم نسخة صبري دراجون 2060
Window.clearcolor = (0.05, 0.05, 0.1, 1)

class TerminalOutput(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output = Label(
            text='[b][color=FFD700]🐉 SABRI DRAGON V4 - READY[/color][/b]\n',
            markup=True, size_hint_y=None, font_size='14sp', halign='left', color=(0, 1, 0, 1)
        )
        self.output.bind(texture_size=self.update_height)
        self.add_widget(self.output)
    def update_height(self, *args): self.output.height = self.output.texture_size[1]
    def append(self, text):
        def update(dt): self.output.text = text + '\n' + self.output.text
        Clock.schedule_once(update)

class ToolButton(Button):
    def __init__(self, tool_name, command, **kwargs):
        super().__init__(**kwargs)
        self.text = tool_name
        self.command = command
        self.size_hint_y = None
        self.height = 50
        self.background_color = (0.2, 0.2, 0.3, 1)
        self.bind(on_press=self.run_tool)
    def run_tool(self, instance):
        app = App.get_running_app()
        app.terminal.append(f'[color=FFD700]🚀 Executing: {self.text}[/color]')
        threading.Thread(target=lambda: self.execute(app), daemon=True).start()
    def execute(self, app):
        res = subprocess.getoutput(self.command)
        Clock.schedule_once(lambda dt: app.terminal.append(res))

class SabriDragonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        tabs = TabbedPanel(do_default_tab=False)
        
        # تبويب الشبكات
        net_tab = TabbedPanelItem(text='🌐 Net')
        net_l = BoxLayout(orientation='vertical', padding=10, spacing=5)
        net_l.add_widget(ToolButton('Nmap Scan', 'nmap -F 127.0.0.1'))
        net_tab.add_widget(net_l)
        tabs.add_widget(net_tab)
        
        # تبويب الاختراق
        exp_tab = TabbedPanelItem(text='💀 Exploit')
        exp_l = BoxLayout(orientation='vertical', padding=10, spacing=5)
        exp_l.add_widget(ToolButton('Check MSF', 'msfconsole -v'))
        exp_tab.add_widget(exp_l)
        tabs.add_widget(exp_tab)

        layout.add_widget(tabs)
        self.terminal = TerminalOutput(size_hint_y=0.4)
        layout.add_widget(self.terminal)
        return layout

if __name__ == '__main__':
    SabriDragonApp().run()
