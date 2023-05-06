##########---MODULES-------#########################################
from tkinter.ttk import*
from tkinter import*
from PIL import ImageTk , Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

##########--------COLORS-----########################################
bg_color = '#7FFFD4'
co1='#566FC6'
co2='#000000'

###########-------WINDOWS-------######################################
window = Tk()
window.title("Alarm Clock")
window.geometry('350x150')
window.configure(bg=bg_color)

##############------------FRAMEUP---------############################
frame_line= Frame(window,width=400,height=5,bg=co1)
frame_line.grid(row=0,column=0)

frame_body=Frame(window,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

################---------------FRAME CONFIGURATION----------------##############################
img = Image.open("icons8-alarm-clock-48.png")
img.resize((500,500))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body,height=100, image=img,bg=bg_color)
app_image.place(x=10,y=10)

name= Label(frame_body,text="Alarm", height=1,font=("ivy 18 bold "),bg=bg_color)
name.place(x=87,y=5)


hour= Label(frame_body,text="Hour", height=1,font=("ivy 11 bold "),bg=bg_color,fg=co2)
hour.place(x=87,y=35)
c_hour=Combobox(frame_body,width=3,font=('arial 15'))
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","18","19","20","22","23")
c_hour.current(0)
c_hour.place(x=87,y=55)


minute= Label(frame_body,text="Minutes", height=1,font=("ivy 11 bold "),bg=bg_color,fg=co2)
minute.place(x=147,y=35)
c_minute=Combobox(frame_body,width=3,font=('arial 15'))
c_minute['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","18","19","20","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_minute.current(0)
c_minute.place(x=150,y=55)


second= Label(frame_body,text="Seconds", height=1,font=("ivy 11 bold "),bg=bg_color,fg=co2)
second.place(x=211,y=35)
c_second=Combobox(frame_body,width=4,font=('arial 15'))
c_second['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","18","19","20","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_second.current(0)
c_second.place(x=215,y=55)


period= Label(frame_body,text="Periods", height=1,font=("ivy 11 bold "),bg=bg_color,fg=co2)
period.place(x=282,y=35)
c_period=Combobox(frame_body,width=3,font=('arial 15'))
c_period['values']=("AM","PM")
c_period.current(0)
c_period.place(x=285,y=55)

####################--------PROCEDURE-----------------###################################
def activate_alarm():
    t = Thread(target = alarm)
    t.start()
    
def deactivate_alarm():
    print('deactivate alarm: ', selected.get())
    mixer.music.stop()
    
        

selected=IntVar()


###########------------ACTIVATE BUTTON-----------####################
rad1=Radiobutton(frame_body,text="Activate", height=1,value=1,font=("ivy 12 bold "),bg=bg_color,command = activate_alarm,variable = selected)
rad1.place(x=87,y=95)

####################---------- UPLOADING OF MUSIC-------------################################
def sound_alarm():
    mixer.music.load('ring2-mp3-6551.mp3')
    mixer.music.play()
    selected.set(0)
    
    rad2=Radiobutton(frame_body,text="Deactivate", height=1,value=2,font=("ivy 12 bold "),bg=bg_color,command = deactivate_alarm)
    rad2.place(x=190,y=95)


###########################----------LOGIC----------------#########################################
def alarm():
    while True:
        control = selected.get()
        print(control)


        alarm_hour= c_hour.get()
        alarm_minute= c_minute.get()
        alarm_second= c_second.get()
        alarm_period= c_period.get()
        alarm_period= str(alarm_period).upper()

        now = datetime.now()

        hour =now.strftime("%H")
        minute =now.strftime("%M")
        second =now.strftime("%S")
        period =now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("GOOD MORNING")
                            sound_alarm()

        sleep(1)


###############---------CALLING THE FUNCTIONS-------------####################################

mixer.init()
window.mainloop()
#------------------------------------------------###----------------------------###--------------------------###-----------------###