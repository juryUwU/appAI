from tkinter import *
import tkinter as tk
import requests
import webbrowser
from gtts import gTTS
import speech_recognition as sr
import os
import time
import playsound

HEIGHT = 500
WIDTH = 600
def bmi():
    a = Tk()
    a.title("Chương trình tính chỉ số đo cơ thể")
    a.geometry("300x400")
    a.attributes("-topmost", True)
    #tạo ra label1
    name1 = Label(a, font = ("Arial",10), text = "Nhập Chiều Cao(m): ")
    name1.place(x = 10, y = 10)
    #tạo ra label2
    name2 = Label(a, font = ("Arial",10), text = "Nhập Cân nặng(kg): ")
    name2.place(x = 10, y = 50)
    #tạo ra label3
    #tạo ra entry1
    entry = Entry(a, width = 15, font = ("Time New Roman",10))
    entry.place(x = 130, y = 10)
    entry.focus()
    #tạo ra entry2
    entry2 = Entry(a, width = 15, font = ("Time New Roman",10))
    entry2.place(x = 130, y = 50)
    #def dieukien():
        
    #Tạo ra button
    def anvao():
        name1 = Label(a , font = ("Arial",10), text =  "Chỉ số BMI của bạn là: " + str(float(entry2.get()) /( float(entry.get()) * 2)), fg="red")
        name1.place(x= 20, y = 110)
        name3 = Label(a, font = ("Arial",10), text = "BMI <18,5 : Bạn đang gầy")
        name3.place(x = 10, y = 140)
        #tạo ra label4
        name4 = Label(a, font = ("Arial",10), text = "BMI = 18,5 - 22,9: Bạn đang bình thường")
        name4.place(x = 10, y = 160)
        #tạo ra label5
        name5 = Label(a, font = ("Arial",10), text = "BMI >=23,0 : Bạn đang thừa cân")
        name5.place(x = 10, y = 180)
        #tạo ra label6
        name6 = Label(a, font = ("Arial",10), text = "BMI > 25,0 : Bạn đang béo phì")
        name6.place(x = 10, y = 200)
    but = Button(a, text = "Tính Toán", width = 10, height = 1, font = ("Time New Roman",10), command = anvao )
    but.place(x=105 , y = 80)
def yt():
    webbrowser.open('https://www.youtube.com')
def fb():
    webbrowser.open('https://www.facebook.com')
def msg():
    webbrowser.open('https://www.messenger.com')
def gg():
    webbrowser.open('https://www.google.com')
def wt():
    def test_function(entry):
        print("This is the entry:", entry)
    def format_response(weather):
        try:
            name = weather['name']
            desc = weather['weather'][0]['description']
            temp = weather['main']['temp']

            final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
        except:
            final_str = 'There was a problem retrieving that information'

        return final_str

    def get_weather(city):
        weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()

        label['text'] = format_response(weather)
def calcl():
    LARGE_FONT_STYLE = ("Arial", 40, "bold")
    SMALL_FONT_STYLE = ("Arial", 16)
    DIGITS_FONT_STYLE = ("Arial", 24, "bold")
    DEFAULT_FONT_STYLE = ("Arial", 20)

    OFF_WHITE = "#F8FAFF"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#CCEDFF"
    LIGHT_GRAY = "#F5F5F5"
    LABEL_COLOR = "#25265E"





    class Calculator:
        def __init__(self):
            self.window = tk.Tk()
            self.window.geometry("375x667")
            self.window.resizable(0, 0)
            self.window.title("Calculator")

            self.total_expression = ""
            self.current_expression = ""
            self.display_frame = self.create_display_frame()

            self.total_label, self.label = self.create_display_labels()

            self.digits = {
                7: (1, 1), 8: (1, 2), 9: (1, 3),
                4: (2, 1), 5: (2, 2), 6: (2, 3),
                1: (3, 1), 2: (3, 2), 3: (3, 3),
                0: (4, 2), '.': (4, 1)
            }   
            self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
            self.buttons_frame = self.create_buttons_frame()

            self.buttons_frame.rowconfigure(0, weight=1)
            for x in range(1, 5):
                self.buttons_frame.rowconfigure(x, weight=1)
                self.buttons_frame.columnconfigure(x, weight=1)
            self.create_digit_buttons()
            self.create_operator_buttons()
            self.create_special_buttons()
            self.bind_keys()

        def bind_keys(self):
            self.window.bind("<Return>", lambda event: self.evaluate())
            for key in self.digits:
                self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

            for key in self.operations:
                self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

        def create_special_buttons(self):
            self.create_clear_button()
            self.create_equals_button()
            self.create_square_button()
            self.create_sqrt_button()

        def create_display_labels(self):
            total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                                fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
            total_label.pack(expand=True, fill='both')

            label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                            fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
            label.pack(expand=True, fill='both')

            return total_label, label

        def create_display_frame(self):
            frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
            frame.pack(expand=True, fill="both")
            return frame

        def add_to_expression(self, value):
            self.current_expression += str(value)
            self.update_label()

        def create_digit_buttons(self):
            for digit, grid_value in self.digits.items():
                button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                                borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

        def append_operator(self, operator):
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""
            self.update_total_label()
            self.update_label()

        def create_operator_buttons(self):
            i = 0
            for operator, symbol in self.operations.items():
                button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=lambda x=operator: self.append_operator(x))
                button.grid(row=i, column=4, sticky=tk.NSEW)
                i += 1

        def clear(self):
            self.current_expression = ""
            self.total_expression = ""
            self.update_label()
            self.update_total_label()

        def create_clear_button(self):
            button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.clear)
            button.grid(row=0, column=1, sticky=tk.NSEW)

        def square(self):
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()

        def create_square_button(self):
            button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.square)
            button.grid(row=0, column=2, sticky=tk.NSEW)

        def sqrt(self):
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.update_label()

        def create_sqrt_button(self):
            button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.sqrt)
            button.grid(row=0, column=3, sticky=tk.NSEW)

        def evaluate(self):
            self.total_expression += self.current_expression
            self.update_total_label()
            try:
                self.current_expression = str(eval(self.total_expression))

                self.total_expression = ""
            except Exception as e:
                self.current_expression = "Error"
            finally:
                self.update_label()

        def create_equals_button(self):
            button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.evaluate)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        def create_buttons_frame(self):
            frame = tk.Frame(self.window)
            frame.pack(expand=True, fill="both")
            return frame

        def update_total_label(self):
            expression = self.total_expression
            for operator, symbol in self.operations.items():
                expression = expression.replace(operator, f' {symbol} ')
            self.total_label.config(text=expression)

        def update_label(self):
            self.label.config(text=self.current_expression[:11])

        def run(self):
            self.window.mainloop()


    if __name__ == "__main__":
        calc = Calculator()
        calc.run()


    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)
def onEnter(event):
    print("Enter Pressed")


root = Tk()
root.title("Console")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Consolas"
FONT_BOLD = "Helvetica 13 bold"
def speak(text):
    tts = gTTS(text=text,lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
speak("xin chào")
def send():

    send = "Bạn: " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if (user == "xin chào"):
        txt.insert(END, "\n" + "Hoài Bảo: Tôi có thể giúp gì cho bạn ?") + speak("tôi có thể giúp gì cho bạn ?")

    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Hoài Bảo: bạn muốn tôi làm gì ??") + speak("bạn muốn tôi làm gì ?")

    elif (user == "bạn khoẻ không ?"):
        txt.insert(END, "\n" + "Hoài Bảo: tôi ổn! còn bạn ?") + speak("tôi ổn, còn bạn ?")

    elif (user == "khoẻ" or user == "tôi khoẻ" or user == "tôi vẫn khoẻ"):
        txt.insert(END, "\n" + "Hoài Bảo: tuyệt, tôi có thể giúp gì cho bạn ?") + speak("tuyệt, tôi có thể giúp gì cho bạn ?")
    elif (user == "cảm ơn" or user == "cảm ơn bạn"):
        txt.insert(END, "\n" + "Hoài Bảo: không có gì") + speak("không có gì")

    elif (user == "thời tiết"):
        wt() + txt.insert(END, "\n" + "Hoài Bảo: mở ứng dụng thời tiết")

    elif (user == "youtube"):
        yt() + txt.insert(END, "\n" + "Hoài Bảo: mở youtube") 
        speak("mở youtube")

    elif (user == "facebook"):
        fb() + txt.insert(END, "\n" + "Hoài Bảo: mở facebook") 
        speak("mở facebook")

    elif (user == "google"):
        gg() + txt.insert(END, "\n" + "Hoài Bảo: mở google") 
        speak("mở google")
        
    elif (user == "messenger"):
        msg() + txt.insert(END, "\n" + "Hoài Bảo: mở messenger") 
        speak("mở messenger")

    elif (user == "tính chỉ số cơ thể"):
        bmi() + txt.insert(END, "\n" + "Hoài Bảo: mở ứng dụng BMI")
        speak("mở ứng dụng BMI")

    elif (user == "máy tính"):
        calcl() + txt.insert(END, "\n" + "Hoài Bảo: mở máy tính")
        speak("mở máy tính")


    else:
        txt.insert(END, "\n" + "Hoài Bảo: xin lỗi tôi không thể phản hồi yêu cầu của bạn") + speak("xin lỗi tôi không thể phản hồi yêu cầu của bạn")

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Console", font= 'Consolas', pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="gửi", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()