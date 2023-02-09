import tkinter as tk              
from tkinter import font as tkfont 
import controller as ctr


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
      
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (InitPage, DashboardPage,ReportingPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("InitPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class InitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title = tk.Label(self, text="Aplication", font=controller.title_font)
        title.pack(side="top", fill="x", pady=10)
        usernameLabel = tk.Label(self, text="User Name")
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=self.username)
        usernameLabel.pack(side="top",padx=4,pady=4)
        usernameEntry.pack(side="top",padx=4,pady=4)
        self.password=tk.StringVar()
        passwordLabel=tk.Label(self, text="Password")
        passwordEntry = tk.Entry(self, textvariable=self.password)
        passwordLabel.pack(side="top",padx=4,pady=4)
        passwordEntry.pack(side="top",padx=4,pady=4)
        self.email=tk.StringVar()
        emailLabel=tk.Label(self, text="email")
        emailEntry = tk.Entry(self, textvariable=self.email)
        emailLabel.pack(side="top",padx=4,pady=4)
        emailEntry.pack(side="top",padx=4,pady=4)
        self.fullname=tk.StringVar()
        fullnameLabel=tk.Label(self, text="fullname")
        fullnameEntry = tk.Entry(self, textvariable=self.fullname)
        fullnameLabel.pack(side="top",padx=4,pady=4)
        fullnameEntry.pack(side="top",padx=4,pady=4)
        self.tipousuario=tk.StringVar()
        tipousuarioLabel=tk.Label(self, text="tipousuario")
        tipousuarioEntry = tk.Entry(self, textvariable=self.tipousuario)
        tipousuarioLabel.pack(side="top",padx=4,pady=4)
        tipousuarioEntry.pack(side="top",padx=4,pady=4)
        ButtonSubmit=tk.Button(self, text="get Data",
                            command=self.mostrardata)
        ButtonSubmit.pack(side="top",padx=4,pady=4)
        buttonDashboard = tk.Button(self, text="Go to the DashboardPage",
                           command=lambda: controller.show_frame("DashboardPage"))
        buttonReport = tk.Button(self, text="Go to the ReportingPage",
                           command=lambda: controller.show_frame("ReportingPage"))
        buttonDashboard.pack()
        buttonReport.pack()

        
    def mostrardata(self):
            data=(str(self.username),str(self.password),str(self.email),str(self.fullname),str(self.tipousuario))
            print(type(str(self.username)))
            try:
                ctr.insertUser(data)
            except Exception as e:
                print("error al ingresar data")
                print(e)

class DashboardPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="DashboardPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("InitPage"))
        button.pack()


class ReportingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ReportingPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("InitPage"))
        button2 = tk.Button(self,text="Generate Report", command=self.generateReport)
        button.pack()
        button2.pack()
    def generateReport(self):
        print("generate Report")
        pass

