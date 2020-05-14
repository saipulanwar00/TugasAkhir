#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import Button
from tkinter import messagebox


class Umr(Tk):

    def __init__(self):
        super().__init__()
        self.label1 = Label(
            self,
            text='Selamat datang',
            bg='red',
            fg='yellow',
            font='times 16 bold italic',
            height=2,
            width=21,
            )
        self.label1.pack()
        self.labe = Label(
            self,
            text='Pejuang Rupiah',
            bg='green',
            fg='white',
            font='times 8 bold italic',
            width=45,
            ).pack()
        self.label2 = Label(
            self,
            text='Silahkan Masukan Data Diri Anda Sebelum Cek UMR',
            bg='green',
            fg='black',
            font='times 6 bold',
            width=60,
            )
        self.label2.pack()
        self.labu = Label(self, text='', bg='black', width=60,
                          height=2).pack()
        self.label3 = Label(
            self,
            text='Nama',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            ).pack()
        self.entry1 = Entry(self, width=60)
        self.entry1.pack()
        self.entry1.insert(0, 'Nama')
        self.label4 = Label(
            self,
            text='Pekerjaan',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            )
        self.label4.pack()
        self.entry2 = Entry(self, width=60)
        self.entry2.pack()
        self.entry2.insert(0, 'Pekerjaan')
        self.label5 = Label(
            self,
            text='Tempat Tinggal',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            )
        self.label5.pack()
        self.entry3 = Entry(self, width=60)
        self.entry3.pack()
        self.entry3.insert(0, 'Tempat Tinggal')
        self.button = Button(
            self,
            text='OK',
            bg='orange',
            font='times 6 bold',
            width=60,
            command=self.klik,
            ).pack()
        self.label6 = Label(
            self,
            text='',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            )
        self.label6.pack()
        self.label7 = Label(
            self,
            text='',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            )
        self.label7.pack()
        self.label8 = Label(
            self,
            text='',
            bg='black',
            fg='white',
            font='times 6 italic',
            width=60,
            )
        self.label8.pack()

    def klik(self):
        self.label6.configure(text=str(self.entry1.get()))
        self.label7.configure(text=str(self.entry2.get()))
        self.label8.configure(text=str(self.entry3.get()))
        if self.entry2.get() == 'Buruh':
            self.lb = Label(
                self,
                text='Cek UMR Buruh',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik3,
                ).pack()
        elif self.entry2.get() == 'buruh':
            self.lb = Label(
                self,
                text='Cek UMR Buruh',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik3,
                ).pack()
        elif self.entry2.get() == 'Karyawan Swasta':
            self.lb = Label(
                self,
                text='Cek UMR Karyawan Swasta',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik4,
                ).pack()
        elif self.entry2.get() == 'Karyawan swasta':
            self.lb = Label(
                self,
                text='Cek UMR Karyawan Swasta',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik4,
                ).pack()
        elif self.entry2.get() == 'karyawan Swasta':
            self.lb = Label(
                self,
                text='Cek UMR Karyawan Swasta',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik4,
                ).pack()
        elif self.entry2.get() == 'karyawan swasta':
            self.lb = Label(
                self,
                text='Cek UMR Karyawan Swasta',
                bg='Yellow',
                fg='black',
                font='times 8 bold',
                width=60,
                ).pack()
            self.etry = Entry(self, text='', width=60)
            self.etry.pack()
            self.etry.insert(0, 'Jakarta')
            self.but3 = Button(
                self,
                text='cek',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik4,
                ).pack()
        else:
            self.lb = Label(
                self,
                text='umr untuk pekerjaan ini blm tersedia',
                bg='black',
                fg='white',
                font='times 6 italic',
                width=60,
                ).pack()

    def klik3(self):
        self.lab = Label(self, text=str(self.etry.get())).pack()
        if self.etry.get() == 'Bandung':
            self.lab = Label(self,
                             text='Umr dibandung adalah Rp 3.623.778,91'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'bandung':
            self.lab = Label(self,
                             text='Umr dibandung adalah Rp 3.623.778,91'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'Jakarta':
            self.lab = Label(self,
                             text='UMR di Jakarta Adalah Rp 4.267.349,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'jakarta':
            self.lab = Label(self,
                             text='UMR di Jakarta Adalah Rp 4.267.349,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'Semarang':
            self.lab = Label(self,
                             text='UMR di Semarang Adalah Rp 4,300,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'semarang':
            self.lab = Label(self,
                             text='UMR di Semarang Adalah Rp 4,300,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        else:
            self.lab = Label(self,
                             text='UMR di Daerah ini Belum Tersedia',
                             fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()

    def klik4(self):
        self.lab = Label(self, text=str(self.etry.get())).pack()
        if self.etry.get() == 'Bandung':
            self.lab = Label(self,
                             text='Umr dibandung adalah Rp 4,000,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'bandung':
            self.lab = Label(self,
                             text='Umr dibandung adalah Rp 4,000,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'Jakarta':
            self.lab = Label(self,
                             text='UMR di Jakarta Adalah Rp 4,200,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'jakarta':
            self.lab = Label(self,
                             text='UMR di Jakarta Adalah Rp 4,200,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'Semarang':
            self.lab = Label(self,
                             text='UMR di Semarang Adalah Rp 4,100,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        elif self.etry.get() == 'semarang':
            self.lab = Label(self,
                             text='UMR di Semarang Adalah Rp 4,100,000,-'
                             , fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()
        else:
            self.lab = Label(self,
                             text='UMR di Daerah ini Belum Tersedia',
                             fg='blue', font=('Times', 8)).pack()
            self.b = Button(
                self,
                text='Exit',
                bg='orange',
                font='times 6 bold',
                width=60,
                command=self.klik5,
                ).pack()

    def klik5(self):
        respon = messagebox.askokcancel('Exit', 'Yakin ingin keluar?')
        if respon == 1:
            global root
            root.quit()
        else:
            data = Label(self, text='Yuk cek lagi UMR nya').pack()


root = Umr()
root.mainloop()


			