from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1") #restart

def restart_time():
    os.system("shutdown /r /t 20") #restart with time

def logout():
    os.system("shutdown -1") #logout

def shutDown():
    os.system("Shutdown /s /t 20") #shutdown



st = Tk()
st.title("ShutDown App")
st.geometry("700x500")
st.config(bg="#7F669D")

restart_button = Button(text="Restart", font=("times new roman", 30, "bold"), relief = RAISED, cursor="plus", bg="#F9CEEE", fg="#A25B5B", command=restart)
restart_button.place(x=170, y=20, height="60", width="350")

restart_with_time_button = Button(text="Restart With Time", font=("times new roman", 30, "bold"), relief = RAISED, cursor="plus", bg="#F9CEEE", fg="#A25B5B", command=restart_time)
restart_with_time_button.place(x=170, y=90, height="60", width="350")

logout_button = Button(text="Logout", font=("times new roman", 30, "bold"), relief = RAISED, cursor="plus", bg="#F9CEEE", fg="#A25B5B", command=logout)
logout_button.place(x=170, y=160, height="60", width="350")

shutdown_button = Button(text="ShutDown", font=("times new roman", 30, "bold"), relief = RAISED, cursor="plus", bg="#F9CEEE", fg="#A25B5B", command=shutDown)
shutdown_button.place(x=170, y=230, height="60", width="350")

st.mainloop()



