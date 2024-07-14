import os
import requests
import customtkinter
import json
import tempfile
import threading
import glob
import difflib
import sys
import time
import pyperclip
from valclient.client import Client
from PIL import Image
from io import BytesIO


# a function to auto generate config files
def checkFiles():
    defaultConfig = {
        "agents": {
                "Jett": "add6443a-41bd-e414-f6ad-e58d267f4e95",
                "Reyna": "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
                "Raze": "f94c3b30-42be-e959-889c-5aa313dba261",
                "Yoru": "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
                "Phoenix": "eb93336a-449b-9c1b-0a54-a891f7921d69",
                "Neon": "bb2a4828-46eb-8cd1-e765-15848195d751",
                "Breach": "5f8d3a7f-467b-97f3-062c-13acf203c006",
                "Skye": "6f2a04ca-43e0-be17-7f36-b3908627744d",
                "Sova": "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
                "Kayo": "601dbbe7-43ce-be57-2a40-4abd24953621",
                "Killjoy": "1e58de9c-4950-5125-93e9-a0aee9f98746",
                "Cypher": "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
                "Sage": "569fdd95-4d10-43ab-ca70-79becc718b46",
                "Chamber": "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
                "Omen": "8e253930-4c05-31dd-1b6c-968525494517",
                "Brazil": "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
                "Astra": "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
                "Viper": "707eab51-4836-f488-046a-cda6bf494859",
                "Fade": "dade69B4-4f5a-8528-247b-219e5a1facd6",
                "Gekko": "E370FA57-4757-3604-3648-499E1F642D3F",
                "Deadlock": "CC8B64C8-4B25-4FF9-6E7F-37B4DA43D235",
                "Iso": "0E38B510-41A8-5780-5E8F-568B2A4F2D6C",
                "Clove": "1DBF2EDD-4729-0984-3115-DAA5EED44993",
                "Harbor": "95B78ED7-4637-86D9-7E41-71BA8C293152"
            },
        "regions": {
            "Europe": "eu",
            "North America": "na",
            "Asia Pacific": "ap",
            "Latin America": "latam",
            "Brazil": "br",
            "Korea": "kr"
        },
        "region": "eu",
        "agent": "Reyna",
        "ran": False
    }
    # Check file existance and missing agents and update them
    if os.path.exists('config.json'):
        with open('config.json', 'r') as file:
            currentConfig = json.load(file)

        for agent, id in defaultConfig["agents"].items():
            if agent not in currentConfig["agents"]:
                currentConfig["agents"][agent] = id

        with open('config.json', 'w') as file:
            json.dump(currentConfig, file, indent=4)
    else:
        with open('config.json', 'w') as file:
            json.dump(defaultConfig, file, indent=4)
    defaultTheme = {
        "CTk": {
            "fg_color": ["gray92", "gray14"]
        },
        "CTkToplevel": {
            "fg_color": ["gray92", "gray14"]
        },
        "CTkFrame": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["gray86", "gray17"],
            "top_fg_color": ["gray81", "gray20"],
            "border_color": ["gray65", "gray28"]
        },
        "CTkButton": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["#D03434", "#A11D1D"],
            "hover_color": ["#B22E2E", "#791414"],
            "border_color": ["#3E454A", "#949A9F"],
            "text_color": ["#DCE4EE", "#DCE4EE"],
            "text_color_disabled": ["gray74", "gray60"]
        },
        "CTkLabel": {
            "corner_radius": 0,
            "fg_color": "transparent",
            "text_color": ["gray10", "#DCE4EE"]
        },
        "CTkEntry": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#F9F9FA", "#343638"],
            "border_color": ["#979DA2", "#565B5E"],
            "text_color": ["gray10", "#DCE4EE"],
            "placeholder_text_color": ["gray52", "gray62"]
        },
        "CTkCheckBox": {
            "corner_radius": 6,
            "border_width": 3,
            "fg_color": ["#D03434", "#A11D1D"],
            "border_color": ["#3E454A", "#949A9F"],
            "hover_color": ["#D03434", "#A11D1D"],
            "checkmark_color": ["#DCE4EE", "gray90"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkSwitch": {
            "corner_radius": 1000,
            "border_width": 3,
            "button_length": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["#D03434", "#A11D1D"],
            "button_color": ["gray36", "#D5D9DE"],
            "button_hover_color": ["gray20", "gray100"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkRadioButton": {
            "corner_radius": 1000,
            "border_width_checked": 6,
            "border_width_unchecked": 3,
            "fg_color": ["#D03434", "#A11D1D"],
            "border_color": ["#3E454A", "#949A9F"],
            "hover_color": ["#B22E2E", "#791414"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkProgressBar": {
            "corner_radius": 1000,
            "border_width": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["#D03434", "#A11D1D"],
            "border_color": ["gray", "gray"]
        },
        "CTkSlider": {
            "corner_radius": 1000,
            "button_corner_radius": 1000,
            "border_width": 6,
            "button_length": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["gray40", "#AAB0B5"],
            "button_color": ["#D03434", "#A11D1D"],
            "button_hover_color": ["#B22E2E", "#791414"]
        },
        "CTkOptionMenu": {
            "corner_radius": 6,
            "fg_color": ["#D03434", "#A11D1D"],
            "button_color": ["#B22E2E", "#791414"],
            "button_hover_color": ["#942525", "#661818"],
            "text_color": ["#DCE4EE", "#DCE4EE"],
            "text_color_disabled": ["gray74", "gray60"]
        },
        "CTkComboBox": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#F9F9FA", "#343638"],
            "border_color": ["#979DA2", "#565B5E"],
            "button_color": ["#979DA2", "#565B5E"],
            "button_hover_color": ["#6E7174", "#7A848D"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray50", "gray45"]
        },
        "CTkScrollbar": {
            "corner_radius": 1000,
            "border_spacing": 4,
            "fg_color": "transparent",
            "button_color": ["gray55", "gray41"],
            "button_hover_color": ["gray40", "gray53"]
        },
        "CTkSegmentedButton": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#979DA2", "gray29"],
            "selected_color": ["#D03434", "#A11D1D"],
            "selected_hover_color": ["#B22E2E", "#791414"],
            "unselected_color": ["#979DA2", "gray29"],
            "unselected_hover_color": ["gray70", "gray41"],
            "text_color": ["#DCE4EE", "#DCE4EE"],
            "text_color_disabled": ["gray74", "gray60"]
        },
        "CTkTextbox": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["#F9F9FA", "#1D1E1E"],
            "border_color": ["#979DA2", "#565B5E"],
            "text_color": ["gray10", "#DCE4EE"],
            "scrollbar_button_color": ["gray55", "gray41"],
            "scrollbar_button_hover_color": ["gray40", "gray53"]
        },
        "CTkScrollableFrame": {
            "label_fg_color": ["gray78", "gray23"]
        },
        "DropdownMenu": {
            "fg_color": ["gray90", "gray20"],
            "hover_color": ["gray75", "gray28"],
            "text_color": ["gray10", "gray90"]
        },
        "CTkFont": {
            "macOS": {
            "family": "SF Display",
            "size": 13,
            "weight": "normal"
            },
            "Windows": {
            "family": "Roboto",
            "size": 13,
            "weight": "normal"
            },
            "Linux": {
            "family": "Roboto",
            "size": 13,
            "weight": "normal"
            }
        }
}


    if not os.path.exists('colorTheme.json'):
        with open('colorTheme.json', 'w') as f:
            json.dump(defaultTheme, f, indent=4)
    
# cleaning icons from the temp file so it doesn't fill up storage over time :) kinda stupid
def cleanup_temp_files():
    for temp_file in glob.glob(os.path.join(tempfile.gettempdir(), "*.ico")):
        try:
            os.remove(temp_file)
        except Exception as e:
            print(f"Error deleting file {temp_file}: {e}")
            
cleanup_temp_files()
checkFiles()
# download the icon into a temp file
def download_image_to_tempfile(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".ico")
        image.save(temp_file.name)
        return temp_file.name
    else:
        raise Exception("Failed to download image")
image_url = "http://nuggets.imu-sama.online:2005/3.ico"
image = download_image_to_tempfile(image_url)

agents = {}
playedMatches = []
white_text = "#DCE4EE"
red_text = "#ff0f0f"
blue_text = "#00FFFF"

with open('config.json', 'r') as f:
    config = json.load(f)
    ranBefore = config['ran']
    agents = config['agents']
    region = config['region']
    regions = config['regions']
    selectedAgent = config['agent']

# app colors
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("colorTheme.json")

# app options
app = customtkinter.CTk()
app.title("FuretaPikku")
app.geometry("900x600")
app.resizable(False, False)
app.iconbitmap(image)

# Top image
img = customtkinter.CTkImage(light_image=Image.open(image), dark_image=Image.open(image), size=(170,170))
imgLabel = customtkinter.CTkLabel(app, text="", image=img)
imgLabel.place(relx= 0.45, rely= 0.08)
def findKeysByValue(ob, value):
    value_lower = value.lower()
    keys = [key for key, val in ob.items() if isinstance(val, str) and val.lower() == value_lower]
    return keys

# region select frame and options
def selRegion():
    newRegion = str(comboboxRegion.get())
    newRegion = regions[newRegion]
    with open('config.json', 'w') as f:
            config['region'] = newRegion
            config['ran'] = True
            json.dump(config, f, indent=4)
    comboboxAgents.configure(state= "readonly")
    comboboxRegion.configure(state= "disabled")
    buttonStart.configure(state= "normal", command=startButton)
    buttonStartDodge.configure(state="normal", command=lambda: start(dodge= True, check= False, names=False))
    buttonStartCheck.configure(state="normal", command=lambda: start(dodge= False, check= True, names=False))
    buttonStartNames.configure(state="normal", command=lambda: start(dodge= False, check= False, names=True))
    buttonRegion.configure(text="Change", command=changeRegion)
    buttonStartText.configure(text= "Select Your Agent and then Press Start", text_color=white_text)
def changeRegion():
    with open('config.json', 'w') as f:
            config['region'] = "eu"
            config['ran'] = False
            json.dump(config, f, indent=4)
    comboboxAgents.configure(state= "disabled")
    buttonStart.configure(state= "disabled")
    buttonStartDodge.configure(state="disabled")
    buttonStartCheck.configure(state="disabled")
    buttonStartNames.configure(state="disabled")
    comboboxRegion.configure(state= "readonly")
    buttonStartText.configure(text= "Select Your Agent and then Press Start", text_color=white_text)
    buttonRegion.configure(text= "Start", command=selRegion)
region_frame = customtkinter.CTkFrame(master=app,width=435 ,height=120, corner_radius=20)
region_frame.pack(padx=20, pady=20)
region_frame.place(relx=0.015, rely =0.45)
comboboxRegion = customtkinter.CTkComboBox(master=region_frame, values=list(regions.keys()), state="readonly")
comboboxRegion.place(relx=0.5, rely=0.3, anchor= customtkinter.CENTER)
buttonRegion = customtkinter.CTkButton(master=region_frame, text="Select", command=selRegion)
buttonRegion.place(relx=0.5, rely=0.6, anchor= customtkinter.CENTER)
'''
Advanced Scrollable Dropdown class for customtkinter widgets
Author: Akash Bora
'''
class CTkScrollableDropdown(customtkinter.CTkToplevel):
    
    def __init__(self, attach, x=None, y=None, button_color=None, height: int = 200, width: int = None,
                 fg_color=None, button_height: int = 20, justify="center", scrollbar_button_color=None,
                 scrollbar=True, scrollbar_button_hover_color=None, frame_border_width=2, values=[],
                 command=None, image_values=[], alpha: float = 0.97, frame_corner_radius=20, double_click=False,
                 resize=True, frame_border_color=None, text_color=None, autocomplete=False, 
                 hover_color=None, **button_kwargs):
        
        super().__init__(master=attach.winfo_toplevel(), takefocus=1)
        
        self.focus()
        self.lift()
        self.alpha = alpha
        self.attach = attach
        self.corner = frame_corner_radius
        self.padding = 0
        self.focus_something = False
        self.disable = True
        self.update()
        
        if sys.platform.startswith("win"):
            self.after(100, lambda: self.overrideredirect(True))
            self.transparent_color = self._apply_appearance_mode(self._fg_color)
            self.attributes("-transparentcolor", self.transparent_color)
        elif sys.platform.startswith("darwin"):
            self.overrideredirect(True)
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
            self.focus_something = True
        else:
            self.overrideredirect(True)
            self.transparent_color = '#000001'
            self.corner = 0
            self.padding = 18
            self.withdraw()

        self.hide = True
        self.attach.bind('<Configure>', lambda e: self._withdraw() if not self.disable else None, add="+")
        self.attach.winfo_toplevel().bind('<Configure>', lambda e: self._withdraw() if not self.disable else None, add="+")
        self.attach.winfo_toplevel().bind("<ButtonPress>", lambda e: self._withdraw() if not self.disable else None, add="+")        
        self.bind("<Escape>", lambda e: self._withdraw() if not self.disable else None, add="+")
        
        self.attributes('-alpha', 0)
        self.disable = False
        self.fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if fg_color is None else fg_color
        self.scroll_button_color = customtkinter.ThemeManager.theme["CTkScrollbar"]["button_color"] if scrollbar_button_color is None else scrollbar_button_color
        self.scroll_hover_color = customtkinter.ThemeManager.theme["CTkScrollbar"]["button_hover_color"] if scrollbar_button_hover_color is None else scrollbar_button_hover_color
        self.frame_border_color = customtkinter.ThemeManager.theme["CTkFrame"]["border_color"] if frame_border_color is None else frame_border_color
        self.button_color = customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"] if button_color is None else button_color
        self.text_color = customtkinter.ThemeManager.theme["CTkLabel"]["text_color"] if text_color is None else text_color
        self.hover_color = customtkinter.ThemeManager.theme["CTkButton"]["hover_color"] if hover_color is None else hover_color
        
        
        if scrollbar is False:
            self.scroll_button_color = self.fg_color
            self.scroll_hover_color = self.fg_color
            
        self.frame = customtkinter.CTkScrollableFrame(self, bg_color=self.transparent_color, fg_color=self.fg_color,
                                        scrollbar_button_hover_color=self.scroll_hover_color,
                                        corner_radius=self.corner, border_width=frame_border_width,
                                        scrollbar_button_color=self.scroll_button_color,
                                        border_color=self.frame_border_color)
        self.frame._scrollbar.grid_configure(padx=3)
        self.frame.pack(expand=True, fill="both")
        self.dummy_entry = customtkinter.CTkEntry(self.frame, fg_color="transparent", border_width=0, height=1, width=1)
        self.no_match = customtkinter.CTkLabel(self.frame, text="No Match")
        self.height = height
        self.height_new = height
        self.width = width
        self.command = command
        self.fade = False
        self.resize = resize
        self.autocomplete = autocomplete
        self.var_update = customtkinter.StringVar()
        self.appear = False
        
        if justify.lower()=="left":
            self.justify = "w"
        elif justify.lower()=="right":
            self.justify = "e"
        else:
            self.justify = "c"
            
        self.button_height = button_height
        self.values = values
        self.button_num = len(self.values)
        self.image_values = None if len(image_values)!=len(self.values) else image_values
        
        self.resizable(width=False, height=False)
        self.transient(self.master)
        self._init_buttons(**button_kwargs)

        # Add binding for different ctk widgets
        if double_click or type(self.attach) is customtkinter.CTkEntry or type(self.attach) is customtkinter.CTkComboBox:
            self.attach.bind('<Double-Button-1>', lambda e: self._iconify(), add="+")
        else:
            self.attach.bind('<Button-1>', lambda e: self._iconify(), add="+")

        if type(self.attach) is customtkinter.CTkComboBox:
            self.attach._canvas.tag_bind("right_parts", "<Button-1>", lambda e: self._iconify())
            self.attach._canvas.tag_bind("dropdown_arrow", "<Button-1>", lambda e: self._iconify())
            if self.command is None:
                self.command = self.attach.set
              
        if type(self.attach) is customtkinter.CTkOptionMenu:
            self.attach._canvas.bind("<Button-1>", lambda e: self._iconify())
            self.attach._text_label.bind("<Button-1>", lambda e: self._iconify())
            if self.command is None:
                self.command = self.attach.set
                
        self.attach.bind("<Destroy>", lambda _: self._destroy(), add="+")
        
        self.update_idletasks()
        self.x = x
        self.y = y

        if self.autocomplete:
            self.bind_autocomplete()
            
        self.deiconify()
        self.withdraw()

        self.attributes("-alpha", self.alpha)

    def _destroy(self):
        self.after(500, self.destroy_popup)
        
    def _withdraw(self):
        if self.winfo_viewable() and self.hide:
            self.withdraw()
        
        self.event_generate("<<Closed>>")
        self.hide = True

    def _update(self, a, b, c):
        self.live_update(self.attach._entry.get())
        
    def bind_autocomplete(self, ):
        def appear(x):
            self.appear = True
            
        if type(self.attach) is customtkinter.CTkComboBox:
            self.attach._entry.configure(textvariable=self.var_update)
            self.attach._entry.bind("<Key>", appear)
            self.attach.set(self.values[0])
            self.var_update.trace_add('write', self._update)
            
        if type(self.attach) is customtkinter.CTkEntry:
            self.attach.configure(textvariable=self.var_update)
            self.attach.bind("<Key>", appear)
            self.var_update.trace_add('write', self._update)
        
    def fade_out(self):
        for i in range(100,0,-10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/100)
            
    def fade_in(self):
        for i in range(0,100,10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/100)
            
    def _init_buttons(self, **button_kwargs):
        self.i = 0
        self.widgets = {}
        for row in self.values:
            self.widgets[self.i] = customtkinter.CTkButton(self.frame,
                                                          text=row,
                                                          height=self.button_height,
                                                          fg_color=self.button_color,
                                                          text_color=self.text_color,
                                                          image=self.image_values[self.i] if self.image_values is not None else None,
                                                          anchor=self.justify,
                                                          hover_color=self.hover_color,
                                                          command=lambda k=row: self._attach_key_press(k), **button_kwargs)
            self.widgets[self.i].pack(fill="x", pady=2, padx=(self.padding, 0))
            self.i+=1
 
        self.hide = False
            
    def destroy_popup(self):
        self.destroy()
        self.disable = True

    def place_dropdown(self):
        self.x_pos = self.attach.winfo_rootx() if self.x is None else self.x + self.attach.winfo_rootx()
        self.y_pos = self.attach.winfo_rooty() + self.attach.winfo_reqheight() + 5 if self.y is None else self.y + self.attach.winfo_rooty()
        self.width_new = self.attach.winfo_width() if self.width is None else self.width
        
        if self.resize:
            if self.button_num<=5:      
                self.height_new = self.button_height * self.button_num + 55
            else:
                self.height_new = self.button_height * self.button_num + 35
            if self.height_new>self.height:
                self.height_new = self.height

        self.geometry('{}x{}+{}+{}'.format(self.width_new, self.height_new,
                                           self.x_pos, self.y_pos))
        self.fade_in()
        self.attributes('-alpha', self.alpha)
        self.attach.focus()

    def _iconify(self):
        if self.attach.cget("state")=="disabled": return
        if self.disable: return
        if self.winfo_ismapped():
            self.hide = False
        if self.hide:
            self.event_generate("<<Opened>>")      
            self.focus()
            self.hide = False
            self.place_dropdown()
            self._deiconify()  
            if self.focus_something:
                self.dummy_entry.pack()
                self.dummy_entry.focus_set()
                self.after(100, self.dummy_entry.pack_forget)
        else:
            self.withdraw()
            self.hide = True
            
    def _attach_key_press(self, k):
        self.event_generate("<<Selected>>")
        self.fade = True
        if self.command:
            self.command(k)
        self.fade = False
        self.fade_out()
        self.withdraw()
        self.hide = True
            
    def live_update(self, string=None):
        if not self.appear: return
        if self.disable: return
        if self.fade: return
        if string:
            string = string.lower()
            self._deiconify()
            i=1
            for key in self.widgets.keys():
                s = self.widgets[key].cget("text").lower()
                text_similarity = difflib.SequenceMatcher(None, s[0:len(string)], string).ratio()
                similar = s.startswith(string) or text_similarity > 0.75
                if not similar:
                    self.widgets[key].pack_forget()
                else:
                    self.widgets[key].pack(fill="x", pady=2, padx=(self.padding, 0))
                    i+=1
                    
            if i==1:
                self.no_match.pack(fill="x", pady=2, padx=(self.padding, 0))
            else:
                self.no_match.pack_forget()
            self.button_num = i
            self.place_dropdown()
            
        else:
            self.no_match.pack_forget()
            self.button_num = len(self.values)
            for key in self.widgets.keys():
                self.widgets[key].destroy()
            self._init_buttons()
            self.place_dropdown()
            
        self.frame._parent_canvas.yview_moveto(0.0)
        self.appear = False
        
    def insert(self, value, **kwargs):
        self.widgets[self.i] = customtkinter.CTkButton(self.frame,
                                                       text=value,
                                                       height=self.button_height,
                                                       fg_color=self.button_color,
                                                       text_color=self.text_color,
                                                       hover_color=self.hover_color,
                                                       anchor=self.justify,
                                                       command=lambda k=value: self._attach_key_press(k), **kwargs)
        self.widgets[self.i].pack(fill="x", pady=2, padx=(self.padding, 0))
        self.i+=1
        self.values.append(value)
        
    def _deiconify(self):
        if len(self.values)>0:
            self.deiconify()

    def popup(self, x=None, y=None):
        self.x = x
        self.y = y
        self.hide = True
        self._iconify()

    def hide(self):
        self._withdraw()
        
    def configure(self, **kwargs):
        if "height" in kwargs:
            self.height = kwargs.pop("height")
            self.height_new = self.height
            
        if "alpha" in kwargs:
            self.alpha = kwargs.pop("alpha")
            
        if "width" in kwargs:
            self.width = kwargs.pop("width")
            
        if "fg_color" in kwargs:
            self.frame.configure(fg_color=kwargs.pop("fg_color"))
            
        if "values" in kwargs:
            self.values = kwargs.pop("values")
            self.image_values = None
            self.button_num = len(self.values)
            for key in self.widgets.keys():
                self.widgets[key].destroy()
            self._init_buttons()
 
        if "image_values" in kwargs:
            self.image_values = kwargs.pop("image_values")
            self.image_values = None if len(self.image_values)!=len(self.values) else self.image_values
            if self.image_values is not None:
                i=0
                for key in self.widgets.keys():
                    self.widgets[key].configure(image=self.image_values[i])
                    i+=1
                    
        if "button_color" in kwargs:
            for key in self.widgets.keys():
                self.widgets[key].configure(fg_color=kwargs.pop("button_color"))
                
        if "font" in kwargs:
            for key in self.widgets.keys():
                self.widgets[key].configure(font=kwargs.pop("font"))
                
        if "hover_color" not in kwargs:
            kwargs["hover_color"] = self.hover_color
        
        for key in self.widgets.keys():
            self.widgets[key].configure(**kwargs)


# agent select frame and options
agent_frame = customtkinter.CTkFrame(master=app,width=435 ,height=120, corner_radius=20)
agent_frame.pack(padx=20, pady=20)
agent_frame.place(relx=0.51, rely =0.45)
comboboxAgents = customtkinter.CTkComboBox(master=agent_frame, values=list(agents.keys()), state="readonly")
comboboxAgents.set(value=selectedAgent)
comboboxAgents.place(relx=0.5, rely=0.48, anchor= customtkinter.CENTER)
sct = CTkScrollableDropdown(comboboxAgents, values=list(agents.keys()), autocomplete= False)
buttonAgentText = customtkinter.CTkLabel(master=agent_frame, text="Select Your Agent To Start Locking in First:")
buttonAgentText.place(relx=0.5, rely=0.25, anchor= customtkinter.CENTER)

#start frame and options

start_frame = customtkinter.CTkFrame(master=app,width=777 ,height=120, corner_radius=20)
start_frame.pack(padx=20, pady=20)
start_frame.place(relx=0.08, rely =0.7)
buttonStart = customtkinter.CTkButton(master=start_frame, text="Start", state="disabled")
buttonStart.place(relx=0.5, rely=0.4, anchor= customtkinter.CENTER)
buttonStartDodge = customtkinter.CTkButton(master=start_frame, text="Dodge", state="disabled", width= 85)
buttonStartDodge.place(relx=0.35, rely=0.4, anchor= customtkinter.CENTER)
buttonStartCheck = customtkinter.CTkButton(master=start_frame, text="Check Side", state="disabled", width= 85)
buttonStartCheck.place(relx=0.65, rely=0.4, anchor= customtkinter.CENTER)
buttonStartNames = customtkinter.CTkButton(master=start_frame, text="Get Hidden Names", state="disabled", width= 85)
buttonStartNames.place(relx=0.88, rely=0.4, anchor= customtkinter.CENTER)
buttonStartText = customtkinter.CTkLabel(master=start_frame, text="Pick your Agent or Action and Start :)", text_color=white_text)
buttonStartText.place(relx=0.5, rely=0.7, anchor= customtkinter.CENTER)


def stop():
    global running
    running = False
    buttonStart.configure(text="Start", command=startButton)

def start(dodge=False, check=False, names=False):
    print("Starting...")
    global running
    if ((dodge == False) and (check == False) and (names==False)):
        print("running set to True")
        running = True
    with open('config.json', 'r') as f:
        newconfig = json.load(f)
        agents = newconfig['agents']
        region = newconfig['region']
    client = Client(region=region)
    try:
        client.activate()
    except Exception as e:
        buttonStartText.configure(text="Looks like VALORANT isn't running", text_color=red_text)
        print(f'{e}')
        return
    if (dodge == True) or (check == True) or (names == True):
        sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
        if ((sessionState == "PREGAME") or (sessionState == "INGAME")):
            if sessionState == "PREGAME" and names == False:
                if (dodge == True):
                    buttonStartText.configure(text='Agent Select Screen Found', text_color=white_text)
                    client.pregame_quit_match()
                    buttonStartText.configure(text='Successfully dodged the Match', text_color=white_text)
                    return
                if (check == True):
                    buttonStartText.configure(text='Agent Select Screen Found', text_color=white_text)
                    ally = client.pregame_fetch_match()['AllyTeam']
                    ally_team = ally['TeamID']
                    ally_result = "Null"
                    side_color = "#DCE4EE"
                    if (ally_team == 'Red'):
                        ally_result = 'Attacker'
                        side_color = red_text
                    elif (ally_team == 'Blue'):
                        ally_result = 'Defender'
                        side_color = blue_text

                    buttonStartText.configure(text=f'you are: {ally_result}', text_color=side_color)
                    return
            elif sessionState != "PREGAME" and names == False:
                buttonStartText.configure(text='You Must Be In Agent Select !!', text_color=red_text)
                return
            elif sessionState == "INGAME" and names == True:
                buttonStartText.configure(text='Getting Hidden Names', text_color=white_text)
                matchId = client.coregame_fetch_player()['MatchID']
                currentMatch = client.coregame_fetch_match(matchId)
                players = []
                for player in currentMatch['Players']:
                    if(player['Subject'] == client.puuid) or (player['PlayerIdentity']['Incognito'] == False):
                        continue
                    players.append(player)
                if not players:
                    buttonStartText.configure(text='No Hidden Names Found', text_color=red_text)
                    return
                else:
                    buttonStartText.configure(text='Found Hidden Names !!', text_color=white_text)
                    newWindow = customtkinter.CTkToplevel(app)
                    newWindow.geometry("400x390")
                    newWindow.title("FuretaPikku Agent Names")
                    newWindow.resizable(0, 0)
                    newWindow.after(250, lambda: newWindow.iconbitmap(image))
                    newWindow.grab_set()
                    mainFrame = customtkinter.CTkScrollableFrame(newWindow, 300, 300, 20)
                    button = customtkinter.CTkLabel(mainFrame, text="Hidden Names Click To Copy:")
                    button.pack(pady=5, anchor="nw")
                    mainFrame.pack(padx= 20, pady= 10)
                    def kill():
                        newWindow.destroy()
                        newWindow.update()
                    doneButton = customtkinter.CTkButton(newWindow, text="Done", command=kill)
                    doneButton.pack(padx=20,pady=5)
                    for hiddenPlayer in players:
                        ally_team = hiddenPlayer['TeamID']
                        ally_result = "Null"
                        side_color = "#DCE4EE"
                        if (ally_team == 'Red'):
                            ally_result = 'Attacker'
                            side_color = red_text
                        elif (ally_team == 'Blue'):
                            ally_result = 'Defender'
                            side_color = blue_text
                        agent_keys = findKeysByValue(agents, hiddenPlayer['CharacterID'])
                        agent = agent_keys[0] if agent_keys else "Undefined"
                        playerId = hiddenPlayer['Subject']
                        playerNameData = client.put(
                            endpoint="/name-service/v2/players", 
                            endpoint_type="pd", 
                            json_data=[playerId]
                        )[0]
                        playerName = playerNameData['GameName']
                        playerTag = f"#{playerNameData['TagLine']}"
                        fullName = f"{playerName}{playerTag}"
                        def copyNames():
                            pyperclip.copy(fullName)
                        button = customtkinter.CTkButton(mainFrame, text=f"{ally_result} {agent}: {playerName}{playerTag}", corner_radius=30, command=copyNames, text_color=side_color)
                        button.pack(pady=5, anchor="nw")
                return
            elif sessionState != "INGAME" and names== True:
                buttonStartText.configure(text='You Must Be Pass The Agent Select !!', text_color=red_text)
                return
            return
        else:
            buttonStartText.configure(text='Start a Game First !!', text_color=red_text)
            return
    preferredAgent = str(comboboxAgents.get())
    with open('config.json', 'w') as f:
        config['agent'] = preferredAgent
        json.dump(config, f, indent=4)
    buttonStart.configure(text="Stop", command=stop)
    buttonStartText.configure(text="Waiting For a Match to Begin...", text_color=white_text)
    while running:
        try:
            print("looping")
            sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
            if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in playedMatches) and (preferredAgent in agents.keys())):
                buttonStartText.configure(text='Agent Select Screen Found', text_color= white_text)
                client.pregame_select_character(agents[preferredAgent])
                client.pregame_lock_character(agents[preferredAgent])
                playedMatches.append(client.pregame_fetch_match()['ID'])
                ally = client.pregame_fetch_match()['AllyTeam']
                ally_team = ally['TeamID']
                ally_result = "Null"
                side_color = "#DCE4EE"
                if (ally_team == 'Red'):
                    ally_result = 'Attacker'
                    side_color = red_text
                elif (ally_team == 'Blue'):
                    ally_result = 'Defender'
                    side_color = blue_text
                buttonStartText.configure(text=f'you are: {ally_result}\nLocked {preferredAgent}', text_color=side_color) 
            time.sleep(1)
        except Exception as e:
            print('', end='')

def startButton():
    print("targeting Thread function")
    selThread = threading.Thread(target=start)
    print("Starting thread process")
    selThread.start()

if ranBefore != True:
    comboboxRegion.set(value= findKeysByValue(regions, region)[0])
    comboboxAgents.configure(state="disabled")
    buttonStartText.configure(text="Please Select Your Region First", text_color=white_text)
elif ranBefore == True:
    comboboxRegion.set(value= findKeysByValue(regions, region)[0])
    comboboxRegion.configure(state="disabled")
    buttonRegion.configure(text="Change", command= changeRegion)
    buttonStart.configure(state="normal", command= startButton)
    buttonStartDodge.configure(state="normal", command=lambda: start(dodge= True, check= False, names=False))
    buttonStartCheck.configure(state="normal", command=lambda: start(dodge= False, check= True, names=False))
    buttonStartNames.configure(state="normal", command=lambda: start(dodge=False, check=False, names=True))
app.mainloop()
