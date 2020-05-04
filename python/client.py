#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import re



def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            if msg.startswith("*"):
                msg_list.insert(tkinter.END, msg)
            else:
                msg=msg.split('+')
                listBox.delete(0,tkinter.END)
                for i in msg:                    
                    listBox.insert(tkinter.END,i)
        except OSError:  
            print('breakReceive')
            break

counter=1
def send(event=None):
    global counter
    msg = my_msg.get()
    name=my_msg2.get()
    my_msg.set("")
    if counter==1:
        send_button_name["state"] = "normal"
        my_msg2.set(msg)
        counter = 2
        selectMember_button["state"] = "normal"
    client_socket.send(bytes(msg, "utf8"))
    client_socket.send(bytes(name, "utf8"))

    if msg == "{quit}":
        client_socket.close()
        top.quit()



def on_closing(event=None):
    my_msg.set("{quit}")
    send()


def receiveName(event=None):
    msg='gtr'
    name=my_msg2.get()
    client_socket.send(bytes(msg, "utf8"))
    client_socket.send(bytes(name, "utf8"))
    
def onselect(evt):
    """
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    my_msg2.set(value)
    """
    values = [listBox.get(idx) for idx in listBox.curselection()]
    my_msg2.set(values[0])
   
position=22   
def selectMember():
    global position
    reslist = list()
    name=selectmember.get()
    listBoxGrup=tkinter.Listbox(top,height=7, width=13)
    listBoxGrup.place(x=10, y=position+22)
    labelListBoxGrup=tkinter.Label(top, text=name,bg='LightBlue1',font=("Courier", 9))
    labelListBoxGrup.place(x=26, y=position)
    seleccion = listBox.curselection()
    for i in seleccion:
        entrada = listBox.get(i)
        reslist.append(entrada)
    for val in reslist:
        listBoxGrup.insert(tkinter.END,val)

    position+=140

    

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame) 

msg_list = tkinter.Listbox(messages_frame, height=20, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send,bg='SkyBlue1',font=("Courier", 9))
send_button.pack()
send_button_name = tkinter.Button(top, text="arkadasları getir", command=receiveName,bg='#856ff8',font=("Courier", 9))
send_button_name.pack()
send_button_name["state"] = "disabled"
 
listBox=tkinter.Listbox(top,height=16, width=18,selectmode = "multiple")
listBox.place(x=740, y=30)
labelListBox=tkinter.Label(top, text="kayitli kullanicilar",bg='#856ff8',font=("Courier", 9))
labelListBox.place(x=740, y=10)
listBox.bind('<<ListboxSelect>>', onselect)


labelGrup=tkinter.Label(top, text='gruplarım',bg='#856ff8',font=("Courier", 9))
labelGrup.place(x=5, y=5)
selectmemberlabel=tkinter.Label(top, text="grup adı giriniz",bg='#856ff8',font=("Courier", 9))
selectmemberlabel.place(x=735, y=410)
selectmember=tkinter.StringVar()
selectmember.set("")
selectmembere1 = tkinter.Entry(top,textvariable=selectmember)
selectmembere1.place(x=735, y=430)
selectMember_button = tkinter.Button(top, text="grup oluştur", command=selectMember,bg='SkyBlue1',font=("Courier", 9))
selectMember_button.place(x=735, y=450)
#selectMember_button.pack()
selectMember_button["state"] = "disabled"


label=tkinter.Label(top, text="iletisim kurulacak kisi",bg='#856ff8',font=("Courier", 9))
label.place(x=733, y=345)
my_msg2=tkinter.StringVar()
my_msg2.set("")
e1 = tkinter.Entry(top,textvariable=my_msg2)
e1.place(x=735, y=375)




top.protocol("WM_DELETE_WINDOW", on_closing)
top.geometry("945x580")
top.configure(bg='#856ff8')
              
              

HOST = "127.0.0.1" 
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)



receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  
















