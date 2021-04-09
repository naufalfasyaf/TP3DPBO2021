#Nama       : Naufal Fasya Faddillah
#NIM        : 1905166

from tkinter import *
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("TP3 DPBO")
root.geometry('700x500')


#Bagian Perintah
def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="About", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Nama : Naufal Fasya Faddillah \n NIM : 1905166 ", anchor="w").grid(row=0, column=0, sticky="w")
    d_exit = Button(d_frame, text="Exit", command=top.destroy)
    d_exit.grid(row=1, column=0)


def inputdata():
    hari = hari_input.get()
    waktu = waktu_input.get()
    jenis_workout = jenis_wo_input.get()

    w1 = "push"
    w2 = "pull"
    w3 = "abs"
    w4 = "cardio"

    #Proses Masuk Data
    file = open("data.txt", "w")
    file.write("Hari    : " + hari + "\n")
    file.write("Waktu   : " + waktu + "\n")
    if(jenis_workout == w1):
        file.write("Workout : " + jenis_workout + "\n")
        file.write("1. Pushup Diamond 3 x 10Rep" + "\n")
        file.write("2. Pushup Wide Grip 3 x 10Rep" + "\n")
        file.write("3. Pushup Close Grip 3 x 10Rep" + "\n")
        file.write("4. Skull Crusher 3 x 10Rep" + "\n")
    if(jenis_workout == w2):
        file.write("Workout : " + jenis_workout + "\n")
        file.write("1. Close Barbell Curl 3 x 12Rep" + "\n")
        file.write("2. Wide Barbell Curl 3 x 12Rep" + "\n")
        file.write("3. Barbell Pull 3 x 10Rep" + "\n")
        file.write("4. Pull Up 3 x 8Rep" + "\n")
    if(jenis_workout == w3):
        file.write("Workout : " + jenis_workout + "\n")
        file.write("1. Climb Hill 3 x 30sec" + "\n")
        file.write("2. Side Foot Tap 3 x 30sec" + "\n")
        file.write("3. Foot-Up 3 x 10Rep" + "\n")
        file.write("4. V-Up 3 x 8Rep" + "\n")
    if(jenis_workout == w4):
        file.write("Workout : " + jenis_workout + "\n")
        file.write("1. Jog 3 x 5min" + "\n")
        file.write("2. Skipping 3 x 3min" + "\n")
        file.write("3. Scott Rush 3 x 10Rep" + "\n")
        file.write("4. Squat Jump 3 x 10Rep" + "\n")
    file.close()

    print("Data Berhasil Dimasukkan")

    hari_lempar.delete(0, END)
    waktu_lempar.delete(0, END)
    jenis_lempar.delete(0, END)


def bukadata():
    #Proses Buka Data
    file = open("data.txt", "r")
    data = file.read()
    print("Data Workout : \n")
    print(data)

    file.close()

#Bagian Framing
frame3 = tk.Frame(root, width=250, bg="RED")
frame3.pack(fill=tk.X, ipadx=8, ipady=8)

frame1 = tk.Frame(root, width=100)
frame1.pack(fill=tk.X, padx=10, pady=5, ipadx=10, ipady=5)

frame2 = tk.Frame(root, width=100)
frame2.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

frame4 = tk.Frame(root, width=100)
frame4.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

frame5 = tk.Frame(root, width=100)
frame5.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

#Bagian label dalam Framing
l1 = Label(frame1, text="Hari       :", font=(16))
l1.grid(row=0, column=0, padx=10, pady=10)

l2 = Label(frame1, text="Waktu      :", font=(16))
l2.grid(row=1, column=0, padx=10, pady=10)

l3 = Label(frame1, text="Pull/Push/ABS/Cardio   :", font=(16))
l3.grid(row=2, column=0, padx=10, pady=10)

l4 = Label(frame1, text="Minggu ke : ", font=(16))
l4.grid(row=3, column=0, padx=10, pady=10)

l5 = Label(frame1, text="Jenis Kelamin : ", font=(16))
l5.grid(row=4, column=0)

l6 = Label(frame1, text="Workout Favorit : ", font=(16))
l6.grid(row=5, column=0)

#Bagian tombol dalam Framing
button2 = Button(frame2, text='Submit', font=(16), width=20, command=inputdata)
button2.pack()

button3 = Button(frame4, text='Lihat Data', font=(16), width=20, command=bukadata)
button3.pack()

button4 = Button(frame4, text='Hapus Seluruh Data', font=(16), width=20)
button4.pack()

button5 = Button(frame4, text='ABOUT', font=(16), width=20, command=about)
button5.pack()

button6 = Button(frame5, text='Keluar', font=(
    16), width=20, bg="red", command=root.quit)
button6.pack()


#Bagian Customisasi Header
judul = Label(frame3, text="Jadwal Latihan",
              font=('Helvetica', 20, 'bold'), fg="white", bg="red")
judul.pack(fill=X, padx=10)

des = Label(frame3, text="Aplikasi Manage Jadwal Latihan",
            font=(50), fg="white", bg="red")
des.pack()

#Bagian Inisialisasi untuk Memasukkan Data
hari_input = StringVar()
waktu_input = StringVar()
jenis_wo_input = StringVar()
minggu = StringVar()
jk = StringVar()

fav1 = StringVar()
fav2 = StringVar()
fav3 = StringVar()
fav4 = StringVar()

MINGGU = [
    "1",
    "2",
    "3",
    "4"
]

variable = StringVar(root)
variable.set(MINGGU[0])  # default value



#Bagian Memasukkan Data
hari_lempar = Entry(frame1, textvariable=hari_input, font=(16), width=15)
hari_lempar.grid(row=0, column=1)

waktu_lempar = Entry(frame1, textvariable=waktu_input, font=(16), width=15)
waktu_lempar.grid(row=1, column=1)

jenis_lempar = Entry(frame1, textvariable=jenis_wo_input, font=(16), width=15)
jenis_lempar.grid(row=2, column=1)

minggu_lempar = OptionMenu(frame1, *MINGGU)
minggu_lempar.grid(row=3, column=1, padx=10, pady=10)

R1 = Radiobutton(frame1, text="Perempuan", variable=jk, value=1)
R1.grid(row=4, column=1)

R2 = Radiobutton(frame1, text="Laki-laki", variable=jk, value=2)
R2.grid(row=4, column=2)

CB1 = Checkbutton(frame1, text="Push", variable=fav1, onvalue=1, offvalue=0)
CB1.grid(row=5, column=1)

CB2 = Checkbutton(frame1, text="Pull", variable=fav2, onvalue=1, offvalue=0)
CB2.grid(row=5, column=2)

CB3 = Checkbutton(frame1, text="ABS", variable=fav3, onvalue=1, offvalue=0)
CB3.grid(row=5, column=3)

CB4 = Checkbutton(frame1, text="Cardio", variable=fav4, onvalue=1, offvalue=0)
CB4.grid(row=5, column=4)

root.mainloop()