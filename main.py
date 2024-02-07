from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import MDList,IconLeftWidget
from kivymd.app import MDApp
from kivy.uix.popup import Popup



class MainScreen(Screen):
    pass

class DemoScreen(Screen):
    pass
class ImageScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.title = "INFO QUAN DZ"
        self.icon = "NTQ.jpg"
        return Builder.load_string("""
ScreenManager:
    MainScreen:
        name: 'main_screen'
    DemoScreen:
        name: 'demo_screen'
    ImageScreen:
        name: 'demo_image'

<MainScreen>:
    RelativeLayout:
        Image:
            source: 'NTQ.jpg'
            allow_stretch: True
            keep_ratio: False
        Label:
            text:"Chúc bạn một ngày tốt lành"
            color: "black"
            size_hint:None,None
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        Button:
            text: 'Bắt đầu'
            color: "yellow"
            size_hint: None, None
            size: 150, 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.08}
            on_release: app.root.current = 'demo_screen'

<DemoScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'clound.jpg'

    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            Image:
                id: avatar
                size_hint: (1,0.8)
                source: "QuanChelsea.jpg"

            Label:
                text: "QuanHuyDiet"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]

            Label:
                text: "ah929586@gmail.com"
                size_hint_y: None
                font_style: "Caption"
                height: self.texture_size[1]

            MDList:
                OneLineIconListItem:
                    text: "Profile"
                    on_release: app.show_profile_info()
                    IconLeftWidget:
                        icon: "account-circle"
                        on_release: app.show_profile_info()
                OneLineIconListItem:
                    text: "Image"
                    on_release: app.root.current = 'demo_image'
                    IconLeftWidget:
                        icon: "image-outline"
                        on_release: app.root.current = 'demo_image'
                OneLineIconListItem:
                    text: "Logout"
                    on_release: app.root.current = 'main_screen'
                    IconLeftWidget:
                        icon: "logout"
                        on_release: app.root.current = 'main_screen'

<ImageScreen>:
    BoxLayout:
        orientation:"vertical"

        StackLayout:
            orientation: "lr-tb"
            
            Image:
                source: "image/avt.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/AI-FC.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/biggame.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/hongbat.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/5801-FC.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/5801.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/quandz.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/quanPhale.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/thanhxuan.jpg"
                size_hint:(0.25,0.2)
            Image:
                source: "image/thiencam-fc.jpg"
                size_hint:(0.25,0.2)
            
            
        BoxLayout:
            size_hint_y: 0.1
            MDList:
                OneLineIconListItem:
                    text: "Back"
                    on_release: app.root.current = 'demo_screen'
                    IconLeftWidget:
                        icon: "arrow-left"
                        on_release: app.root.current = 'demo_screen'

            

                        
""")        

    

    def show_profile_info(self):
        # Thêm mã xử lý hiển thị thông tin profile ở đây, ví dụ:
        info_layout = BoxLayout(orientation="vertical", padding=10)

        horizontal_layout = BoxLayout(orientation="horizontal")
        icon_widget = IconLeftWidget(icon="account-heart-outline")
        label_widget = Label(text="Độc thân")
        horizontal_layout.add_widget(icon_widget)
        horizontal_layout.add_widget(label_widget)

        # Thêm BoxLayout ngang vào info_layout
        info_layout.add_widget(horizontal_layout)

        horizontal_layout = BoxLayout(orientation="horizontal")
        icon_widget = IconLeftWidget(icon="phone")
        label_widget = Label(text="0382656974")
        horizontal_layout.add_widget(icon_widget)
        horizontal_layout.add_widget(label_widget)

        # Thêm BoxLayout ngang vào info_layout
        info_layout.add_widget(horizontal_layout)

        horizontal_layout = BoxLayout(orientation="horizontal")
        icon_widget = IconLeftWidget(icon="facebook")
        label_widget = Label(text="Nguyễn Tông Quân")
        horizontal_layout.add_widget(icon_widget)
        horizontal_layout.add_widget(label_widget)

        # Thêm BoxLayout ngang vào info_layout
        info_layout.add_widget(horizontal_layout)

        horizontal_layout = BoxLayout(orientation="horizontal")
        icon_widget = IconLeftWidget(icon="instagram")
        label_widget = Label(text="n_tquaan")
        horizontal_layout.add_widget(icon_widget)
        horizontal_layout.add_widget(label_widget)

        # Thêm BoxLayout ngang vào info_layout
        info_layout.add_widget(horizontal_layout)

        popup = Popup(title="Thông tin Profile", content=info_layout, size_hint=(None, None), size=(300, 350))

        popup.open()
    
if __name__ == '__main__':
    MainApp().run()


