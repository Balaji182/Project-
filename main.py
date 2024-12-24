from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser
from kivy.uix.screenmanager import Screen,ScreenManager

K = """#K is a string_Name
Screen:#To get a screen view
    MDNavigationLayout:#Screen sub class,NavigationBar layput
        ScreenManager:#Manages  Screen
            id: screen_manager
            Screen:
                name: "home"#for switching screen id
                BoxLayout:#layout
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "SEVA"#toolbar contant
                        left_action_items: [["menu", lambda x: nav.set_state("toggle")]]#menu icon
                        elevation: 10
                    ScrollView:#scrollview for dat
                        BoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                            spacing: "10dp"
                            padding: "20dp"
                            MDLabel:#Mdlabel for write data
                                text: "NAME: Child Aid Foundation"
                                size_hint_y: None
                                height: self.texture_size[1]# to adjust to screen
                            MDLabel:
                                text: "ADDRESS: Child Aid Foundation - Door No 2(B), \\nDoor No : 40-25-58, CAF Road, Patamatalanka,\\n Vijayawada - 520015 (Near SVS Kalyana Mandapam)\\n Cell: +917411590448"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "OPEN ON MAP:[ref=map1] CLICK TO OPEN MAP[/ref]"#to open map ehen we click
                                markup: True#if it is flase it can be clickble
                                on_ref_press: app.open_map1()
                                size_hint_y: None#condtion for open map
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Sri R R Murthy Vruddhula Seva Samstha"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: House No 16-15-39, Guntur - 522001\\n (Opposite Sri Krishna Kalyana Mandapam)\\n Cell: +9174115 90448"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "OPEN ON MAP:[ref=map2] CLICK TO OPEN MAP[/ref]"
                                markup: True
                                on_ref_press: app.open_map2()
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Navajeevan Bala Bhavan"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: Door No 2B, Andhra Ratna Road, 1st Lane, Gandhi Nagar, Vijayawada - 520003 \\n(Bhavajipet, Behind Lutheran Church)\\n CELL: +9194904 91830"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "OPEN ON MAP:[ref=map3] CLICK TO OPEN MAP[/ref]"
                                markup: True
                                on_ref_press: app.open_map3()
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Tulip Gardens"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: Buthumillupadu, Gannavaram, Gannavaram, Vijayawada - 521101"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "OPEN ON MAP:[ref=map4] CLICK TO OPEN MAP[/ref]"
                                markup: True
                                on_ref_press: app.open_map4()
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Friends Foundation"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: House No 2-258, Chennakesava Nagar, Duggirala, Vijayawada Ho, Vijayawada - 520001\\n (Opposite Duggirala Railway Station, Tenali Road)\\n CELL: +9199635 41004"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Srusti Kartha Social Welfare Association"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: Ck Reddy Road, Gandhi Nagar, Vijayawada - 520003 (Papula Mill Center)\\n CELL: +9193921 32357"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: Golchha Mansion"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "Golchha Mansion  39712, Labbipet, Vijayawada - 520010\\n CELL: +9179 4712 9085"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "OPEN ON MAP:[ref=map5] CLICK TO OPEN MAP[/ref]"
                                markup: True
                                on_ref_press: app.open_map5()
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "NAME: GRACE Bethel Ministries"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "ADDRESS: MANDALIPURAM 4TH LINE, SEETHAYA LANKA, Vijayawada HO, Vijayawada - 520001 (AVANIGADDA KRISHNA DISTRICT)\\n CELL: +9190102 29225"
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: "________________________________________________"
                                size_hint_y: None
                                height: self.texture_size[1]
            Screen:#Registran screen
                name: "registration"
                BoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Register"
                        left_action_items: [["arrow-left", lambda x: app.go_home()]]#arrow icon
                    BoxLayout:
                        orientation: "vertical"
                        padding: "20dp"
                        spacing: "20dp"
                        MDLabel:
                        	text:"*GIVE NAME OF HOME\\n\\n*ADDRESS\\n\\n*EMAIL\\n\\n*PHONE NUMBER\\n\\n*GOOGLE MAP LINK \\n\\n*CORRECTLY FOR GET SLOT IF YOU MISTAKE YOU CAN'T GET A SLOT"
                        MDLabel:#New registration through mail
                            text: "FOR NEW REGISTRATION MAIL TO US [ref=email]\\n                                                                                         CLICKTO REGISTER \\n  \\n  [/ref]"
                            markup: True
                            
                            on_ref_press: app.open_email("hiskniki8@gmail.com")#condtion for click on mail
                            pos_hint: {"center_x": 0.5}
                           

        MDNavigationDrawer:
            id: nav
            ScrollView:
                BoxLayout:#navigation drawer open when we click on menu icon
                    orientation: "vertical"
                    spacing: "8dp"
                    padding: "8dp"
                    size_hint_y: None
                    height: self.minimum_height
                    MDList:
                        OneLineListItem:#list to add List items
                            text: "[b]HOME[/b]"
                            font_style: "H6"
                            spacing: "20dp"
                            padding: "100dp"
                            size_hint_y: None
                            on_release:
                                nav.set_state("close")
                                screen_manager.current = "home"
                        OneLineListItem:
                            text: "[b]REGISTER[/b]"
                            font_style: "H6"
                            spacing: "20dp"
                            padding: "100dp"
                            size_hint_y: None
                            on_release:
                                nav.set_state("close")
                                screen_manager.current = "registration"
"""

class Demo(MDApp):#subclass of MDapp
    def build(self):
        return Builder.load_string(K)#calling string

    def open_email(self, email):
        webbrowser.open(f"mailto:{email}")#calling mail

    def go_home(self):#Open home page
        self.root.ids.screen_manager.current = "home"
    
    def open_map1(self):#opening map
        webbrowser.open("https://maps.app.goo.gl/DbuUUKknyVLiPESRA")
    
    def open_map2(self):
        webbrowser.open("https://maps.app.goo.gl/KvNrhgzagz1cFa929?g_st=ac")

    def open_map3(self):
        webbrowser.open("https://maps.app.goo.gl/benfNwqAfuBmyZMr8?g_st=ac")

    def open_map4(self):
        webbrowser.open("https://maps.app.goo.gl/a7dU4oELDo3j6o86A?g_st=ac")
    
    def open_map5(self):
        webbrowser.open("https://maps.app.goo.gl/EyUrqofRRWvFa3BK8?g_st=ac")

Demo().run()#run the code
