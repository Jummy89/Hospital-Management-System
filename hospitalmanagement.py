from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class hospital:
    def __init__(self, root):
        self.root = root
        self.root.title('Hospital Management System')
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.DrivingusingMachine = StringVar()
        self.HowtouseMedication = StringVar()
        self.PatientId = StringVar()
        self.NoofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.StorageAdvice = StringVar()
        self.nhisNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()



        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        ################### Icon Image ################################
        image_icon = PhotoImage(file="images/icon.png")
        root.iconphoto(False, image_icon)

        #################### Data Frame #######################
        Dataframe=Frame(self.root, bd=20, padx=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft=LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                 font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight=LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                 font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        ####################### Buttons Frame ####################
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)


        ####################### Details Frame ####################
        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        ############## Dataframe Left #################
        lblNameTablet=Label(DataframeLeft, text="Name of Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        conNameTablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets, state="randomly", font=("arial", 12, "bold"), width=33)
        conNameTablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Amiodipine", "Ativan")
        conNameTablet.current(0)
        conNameTablet.grid(row=0, column=1)

        lblRef = Label(DataframeLeft, text="Reference No:", font=("times new roman", 12, "bold"), padx=2)
        lblRef.grid(row=1, column=0, sticky=W)
        txtref=Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        lblDose= Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Dose, width=35)
        lblDose.grid(row=2, column=1)

        lblNoOfTablet = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOfTablet.grid(row=3, column=0, sticky=W)
        lblNoOfTablet = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.NoofTablets, width=35)
        lblNoOfTablet.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Lot:", padx=2,pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        lblLot = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Lot, width=35)
        lblLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        lblIssueDate = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Issuedate, width=35)
        lblIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        lblExpDate = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.ExpDate,width=35)
        lblExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        lblDailyDose = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DailyDose, width=35)
        lblDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        lblSideEffect = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.sideEffect, width=35)
        lblSideEffect.grid(row=8, column=1)

        lblFurtherinformation = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Further Information:",
                                      padx=2)
        lblFurtherinformation.grid(row=0, column=2, sticky=W)
        lblFurtherinformation= Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.FurtherInformation, width=35)
        lblFurtherinformation.grid(row=0, column=3)

        lblBloodpressure = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Blood Pressure:", padx=2,
                                 pady=6)
        lblBloodpressure.grid(row=1, column=2, sticky=W)
        lblBloodpressure = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DrivingusingMachine, width=35)
        lblBloodpressure.grid(row=1, column=3)

        lblStorageAdvice = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="  Storage Advice:", padx=2,
                                 pady=6)
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        lblStorageAdvice = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.StorageAdvice, width=35)
        lblStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Medication:", padx=2,pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        lblMedication= Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.HowtouseMedication, width=35)
        lblMedication.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="PatientId :", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        lblPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientId,width=35)
        lblPatientId.grid(row=4, column=3)

        lblNhisNumber = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="NHIS Number:", padx=2, pady=6)
        lblNhisNumber.grid(row=5, column=2, sticky=W)
        lblNhisNumber = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.nhisNumber,width=35)
        lblNhisNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Name:", padx=2,
                               pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        lblPatientName = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientName, width=35)
        lblPatientName.grid(row=6, column=3)

        lblDob = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDob.grid(row=7, column=2, sticky=W)
        lblDob = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DateofBirth, width=35)
        lblDob.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Address:", padx=2,
                                  pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        lblPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientAddress, width=35)
        lblPatientAddress.grid(row=8, column=3)

        ######################### Data Frame Right ################
        self.txtprecription=Text(DataframeRight,font=("arial",12,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtprecription.grid(row=0, column=0)

        ############### Buttons #######################
        btnprecription=Button(Buttonframe,command=self.iPrectionption,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnprecription.grid(row=0, column=0)

        btnprecriptionData = Button(Buttonframe,command=self.iPrescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial",12,"bold"),width=23, padx=2, pady=6)
        btnprecriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelect = Button(Buttonframe,command=self.idelete, text="Delect", bg="green", fg="white", font=("arial", 12, "bold"),width=23, padx=2, pady=6)
        btnDelect.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command=self.clear, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2,
                         pady=6)
        btnExit.grid(row=0, column=5)

        ############### Table #######################
        ############### Scrollbar #####################
        scroll_x = Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("Nameoftablets", "ref", "dose", "nooftablets", "lot",
                                                                 "issuedate","expdate", "dailydose", "storage", "nhisnumber",
                                                                "pname","dob", "address"),xscrollcommand=scroll_x.set,
                                                                 yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("Nameoftablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhisnumber", text="NHIS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("Nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhisnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.hospital_table.bind('<ButtonRelease-1>', self.get_cursor)

        ##########################DATABASE
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Error", "All Fields Required!!!")
        else:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='mydata')
            cur = con.cursor()
            cur.execute('Insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.Nameoftablets.get(),
                                                                              self.Ref.get(),
                                                                              self.Dose.get(),
                                                                              self.NoofTablets.get(),
                                                                              self.Lot.get(),
                                                                              self.Issuedate.get(),
                                                                              self.ExpDate.get(),
                                                                              self.DailyDose.get(),
                                                                              self.StorageAdvice.get(),
                                                                              self.nhisNumber.get(),
                                                                              self.PatientName.get(),
                                                                              self.DateofBirth.get(),
                                                                              self.PatientAddress.get()
                                                                              ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Record has been Inserted")
            self.fetch_data()

    def update_data(self):
        con =mysql.connector.connect(host='localhost', user='root', password='', database='mydata')
        cur = con.cursor()
        cur.execute("Update students set Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhisnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s",(self.Nameoftablets.get(),
                                                                                                                                                                                                                      self.Dose.get(),
                                                                                                                                                                                                                      self.NoofTablets.get(),
                                                                                                                                                                                                                      self.Lot.get(),
                                                                                                                                                                                                                      self.Issuedate.get(),
                                                                                                                                                                                                                      self.ExpDate.get(),
                                                                                                                                                                                                                      self.DailyDose.get(),
                                                                                                                                                                                                                      self.StorageAdvice.get(),
                                                                                                                                                                                                                      self.nhisNumber.get(),
                                                                                                                                                                                                                      self.PatientName.get(),
                                                                                                                                                                                                                      self.DateofBirth.get(),
                                                                                                                                                                                                                      self.PatientAddress.get(),
                                                                                                                                                                                                                      self.Ref.get()                                                                                                                                                                                                      ))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update", "Record has been Updated")

    def fetch_data(self):
        con=mysql.connector.connect(host='localhost', user='root',password='',database='mydata')
        cur=con.cursor()
        cur.execute('select * from students')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('',END,values=i)
            con.commit()
        con.close()


    def get_cursor(self,event=""):
        curosor_row=self.hospital_table.focus()
        content=self.hospital_table.item(curosor_row)
        row=content['values']
        self.Nameoftablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhisNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateofBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrectionption(self):
        self.txtprecription.insert(END,"Nameoftablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtprecription.insert(END, "Reference No:\t\t\t" + self.Ref.get() + "\n")
        self.txtprecription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtprecription.insert(END, "Number Of Tablets:\t\t\t" + self.NoofTablets.get() + "\n")
        self.txtprecription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtprecription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtprecription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtprecription.insert(END, "daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtprecription.insert(END, "sideEffect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtprecription.insert(END, "FurtherInformation:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtprecription.insert(END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtprecription.insert(END, "DrivingUsingMachine:\t\t\t" + self.DrivingusingMachine.get() + "\n")
        self.txtprecription.insert(END, "PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtprecription.insert(END, "nhisNumber:\t\t\t" + self.nhisNumber.get() + "\n")
        self.txtprecription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtprecription.insert(END, "DateOfBirth:\t\t\t" + self.DateofBirth.get() + "\n")
        self.txtprecription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

    def clear(self):
        self.Nameoftablets.set('')
        self.Ref.set('')
        self.Dose.set('')
        self.sideEffect.set('')
        self.FurtherInformation.set('')
        self.DrivingusingMachine.set('')
        self.HowtouseMedication.set('')
        self.PatientId.set('')
        self.NoofTablets.set('')
        self.Lot.set('')
        self.Issuedate.set('')
        self.ExpDate.set('')
        self.DailyDose.set('')
        self.StorageAdvice.set('')
        self.nhisNumber.set('')
        self.PatientName.set('')
        self.DateofBirth.set('')
        self.PatientAddress.set('')

    def idelete(self):
        con = mysql.connector.connect(host='localhost', user='root', password='', database='mydata')
        mycursor = con.cursor()
        query='Delete from students where Reference_No=%s'
        value=(self.Ref.get(),)
        mycursor.execute(query,value)
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted")
        self.clear()







    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System", "confirm you want to exit")
        if iExit>0:
            root.destroy()
            return











root=Tk()
ob=hospital(root)
root.mainloop()



