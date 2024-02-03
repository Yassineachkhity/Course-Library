from tkinter import *
from tkinter import messagebox
import sys
from PIL import ImageTk, Image
from function import resize_image, on_enter, on_leave, create_entry
import sqlite3
import iagi
import subprocess
import os
import webbrowser

root = Tk()
root.title("Welcome")
root.resizable(False, False)

welcome_page = resize_image('welcome.jpg')
label = Label(root, image=welcome_page)
label.pack()

pages_stack = []


def prec():
    # Function to go back to the previous page
    if pages_stack:
        current_page = pages_stack.pop()
        current_page.withdraw()
        if pages_stack:
            previous_page = pages_stack[-1]
            previous_page.deiconify()
        else:
            root.deiconify()


def ouvrir_pdf_avec_chrome(pdf_path):
    # Utiliser subprocess pour ouvrir Google Chrome avec le fichier PDF
    subprocess.Popen(["start", "", pdf_path], shell=True)


def module():
    """Action qui permet de generer une nouvelle page ou les modules s'affichent
    """

    tk_image4.withdraw()
    global tk_image5
    modules = Toplevel()
    # fct prec
    pages_stack.append(modules)
    tk_image5 = modules
    modules.title("IAGI-1")
    modules.resizable(False, False)

    iagi_image = resize_image('IAGI.png')
    iagi_label = Label(modules, image=iagi_image)
    iagi_label.pack()

    frame2 = Frame(modules, width=290, height=300, bg="#fff")
    frame2.place(x=105, y=180)

    python_image = resize_image('oop.jpg', (250, 40))
    Button(modules, image=python_image, bd=0, bg="#fff", activebackground="#fff", command=oop).place(x=110, y=200)

    ro_image = resize_image('RO.jpg', (320, 40))
    Button(modules, image=ro_image, bd=0, bg="#fff", activebackground="#fff", command=ro).place(x=110, y=270)

    linux_image = resize_image('linux.jpg', (250, 40))
    Button(modules, image=linux_image, bd=0, bg="#fff", activebackground="#fff", command=linux).place(x=110, y=340)

    sdd_image = resize_image('sdd.jpg', (320, 40))
    Button(modules, image=sdd_image, bd=0, bg="#fff", activebackground="#fff", command=sdd).place(x=110, y=410)

    # button pour la barre
    bar_image = resize_image('barre.jpg', (65, 65))
    Button(modules, image=bar_image, bd=0, bg="#fff", activebackground="#fff", command=barre).place(x=0, y=440)

    bar_image = resize_image('barre.jpg', (65, 65))
    Button(modules, image=bar_image, bd=0, bg="#fff", activebackground="#fff", command=barre).place(x=0, y=440)
    # setting du barre
    global nav
    nav = Frame(modules, bg="#042F69", height=600, width=200)
    nav.place(x=-200, y=0)
    global F1, F2
    F1 = Frame(nav, width=170, height=1, bg="#EFB054")
    F2 = Frame(nav, width=170, height=1, bg="#EFB054")

    Button(nav, text="les modules", font=('Microsoft YaHei UI Light', 15, 'bold'), bd=0,
           bg="#042F69", fg="#fff", activebackground="#042F69", activeforeground="gray17", command=module).place(x=25,
                                                                                                                 y=100)

    Button(nav, text="log out", font=('Microsoft YaHei UI Light', 15, 'bold'), bd=0,
           bg="#042F69", fg="#fff", command=root.destroy).place(x=25, y=200)
    global closebtn
    close_image = resize_image('close_bar.jpg', (65, 65))
    closebtn = Button(modules, image=close_image, activebackground="#042F69", bd=0, bg="#042F69", command=barre)

    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(modules, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)
    modules.mainloop()


# parametre du fonction barre

btnstate = False


def barre():
    global btnstate

    if btnstate is True:
        # create animated navbar closing
        for x in range(201):
            nav.place(x=-x, y=0)
            tk_image5.update()

        btnstate = False
        closebtn.place_forget()
        F1.place_forget()
        F2.place_forget()



    else:
        for x in range(-300, 0):
            nav.place(x=x, y=0)
            tk_image5.update()
        btnstate = True
        # Show the close_image button when the nav is open
        closebtn.place(x=0, y=440)
        F1.place(x=15, y=150)
        F2.place(x=15, y=250)


def oop():
    tk_image5.withdraw()
    global tk_python
    python = Toplevel()
    pages_stack.append(python)
    tk_python = python
    python.title("OOP/python")
    python.resizable(False, False)

    oop_image = resize_image('python.jpg')
    oop_label = Label(python, image=oop_image)
    oop_label.pack()
    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(tk_python, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)

    # button du chapitres
    chap1 = resize_image('chap1.jpg', (340, 40))
    Button(tk_python, image=chap1, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Chapitre 5 - Héritage (1).pdf")).place(x=75, y=180)
    chap2 = resize_image('chap2.jpg', (340, 40))
    Button(tk_python, image=chap2, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Chapitre 6 - Gestion des fichiers.pdf")).place(x=85, y=260)
    chap3 = resize_image('chap3.jpg', (320, 40))
    Button(tk_python, image=chap3, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Base de données chap8.pdf")).place(x=80, y=340)

    python.mainloop()


def ro():
    tk_image5.withdraw()
    global tk_ro
    ro = Toplevel()
    pages_stack.append(ro)
    tk_ro = ro
    ro.title("R.O")
    ro.resizable(False, False)

    ro_arriere = resize_image('RO_ar.jpg')
    ro_label = Label(ro, image=ro_arriere)
    ro_label.pack()
    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(tk_ro, image=prec_image, activebackground="#fff", bd=0, bg="#fff", command=prec).place(x=350, y=150)
    # button du chapitres
    chap1 = resize_image('chap1.jpg', (340, 40))
    Button(tk_ro, image=chap1, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("01-Introduction_RO.pdf")).place(x=75, y=180)
    chap2 = resize_image('chap2.jpg', (340, 40))
    Button(tk_ro, image=chap2, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("02-Prog Lineaire - ROPart1.pdf")).place(x=85, y=260)
    chap3 = resize_image('chap3.jpg', (320, 40))
    Button(tk_ro, image=chap3, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("02-Prog Lineaire - ROPart2.pdf")).place(x=80, y=340)
    ro.mainloop()


def sdd():
    tk_image5.withdraw()
    global tk_sdd
    sdd = Toplevel()
    pages_stack.append(sdd)
    tk_sdd = sdd
    sdd.title("SDD")
    sdd.resizable(False, False)

    sdd_arriere = resize_image('sdd_ar.jpg')
    sdd_label = Label(sdd, image=sdd_arriere)
    sdd_label.pack()
    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(tk_sdd, image=prec_image, activebackground="#fff", bd=0, bg="#fff", command=prec).place(x=350, y=100)

    # button du chapitres
    chap1 = resize_image('chap1.jpg', (340, 40))
    Button(tk_sdd, image=chap1, bd=0, bg="#fff", activebackground="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Structure de données en C - Seance 0 - complexite.pdf")).place(x=75,
                                                                                                                  y=180)
    chap2 = resize_image('chap2.jpg', (340, 40))
    Button(tk_sdd, image=chap2, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Structure de données en C - Seance 1 - Listes chainées .pdf")).place(
        x=85, y=260)
    chap3 = resize_image('chap3.jpg', (320, 40))
    Button(tk_sdd, image=chap3, bd=0, activebackground="#fff", bg="#fff",
           command=lambda: ouvrir_pdf_avec_chrome("Structure de données en C - Seance 2 - Listes chainées .pdf")).place(
        x=80, y=340)
    sdd.mainloop()


def linux():
    tk_image5.withdraw()
    global tk_linux
    linux = Toplevel()
    pages_stack.append(linux)
    tk_linux = linux
    linux.title("Linux")
    linux.resizable(False, False)

    linux_arriere = resize_image('linx_ar.jpg')
    linux_label = Label(linux, image=linux_arriere)
    linux_label.pack()
    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(tk_linux, image=prec_image, activebackground="#fff", bd=0, bg="#fff", command=prec).place(x=350, y=100)
    # button du chapitres
    chap1 = resize_image('chap1.jpg', (340, 40))
    Button(tk_linux, image=chap1, bd=0, activebackground="#fff", bg="#fff", command=lambda: ouvrir_pdf_avec_chrome(
        "Systèmes d_exploitation - chap 1 - Introduction UNIX- LINUX.pdf")).place(x=75, y=180)
    chap2 = resize_image('chap2.jpg', (340, 40))
    Button(tk_linux, image=chap2, bd=0, activebackground="#fff", bg="#fff", command=lambda: ouvrir_pdf_avec_chrome(
        "Systèmes d_exploitation - chap 2 - la gestion de fichier sous linux.pdf")).place(x=85, y=260)
    chap3 = resize_image('chap3.jpg', (320, 40))
    Button(tk_linux, image=chap3, bd=0, activebackground="#fff", bg="#fff", command=lambda: ouvrir_pdf_avec_chrome(
        "Systèmes d_exploitation - chap 3 - gestion des utilisateurs et des groupes.pdf")).place(x=80, y=340)

    linux.mainloop()


def create():
    """Action qui permet de sauvegarder les donnees de l'utilisateur dans une base de donnee
    """
    try:
        sql = "INSERT INTO STUDENTS (firstname ,lastname ,email,passwd ) values (?,?,?,?)"
        data = (firstname.get(), lastname.get(), email.get(), password.get())
        iagi.curseur.execute(sql, data)
        iagi.connexion.commit()
        messagebox.showinfo('message', 'Done!')

    except Exception as e:
        # Gérez les exceptions ou affichez un message d'erreur
        messagebox.showerror('Erreur', f'Une erreur s\'est produite: {str(e)}')


def afficher():
    iagi.connexion.row_factory = sqlite3.Row
    iagi.curseur = iagi.connexion.execute("select * from students")  # selection tout le contenue
    for row in iagi.curseur:
        print(row["id"], row["firstname"], row["lastname"], row["email"])


with open("base.txt", "w") as file:
    # Rediriger la sortie standard vers le fichier texte
    sys.stdout = file

    print("les etudiants sont:")
    afficher()


# La sortie est automatiquement restaurée après la fin du bloc 'with'
def check_empty_fields(email, password):
    if not email or not password:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return False
    return True


def login():
    """
       fonction qui permet de creer la page log in ou l'utilisateur doit entrer son email et son
       mot de passe afin de se connecter pour poursuivre un cours
    """
    root.withdraw()
    global tk_image4
    applog = Toplevel()
    # fc prec
    pages_stack.append(applog)
    tk_image4 = applog
    applog.title("Log In")
    applog.resizable(False, False)

    login_image = resize_image('page2_login.jpg')
    login_label = Label(applog, image=login_image)
    login_label.pack()
    frame2 = Frame(applog, width=300, height=360, bg="#fff")
    frame2.place(x=105, y=120)

    # Creation de "entry widgets" avec un text par defaut
    email_entry = create_entry(applog, "email", 130, 200)
    password_entry = create_entry(applog, "password", 130, 280)

    # creation des frames qui soulignent les widgets
    Frame(frame2, width=260, height=1, bg="#004aad").place(x=7, y=110)
    Frame(frame2, width=260, height=1, bg="#004aad").place(x=7, y=190)

    # Creation d'un bouton "next" qui permet d'aller a la page suivante
    next_button_image = resize_image('next_button.jpg', (135, 80))
    Button(applog, image=next_button_image, activebackground="#fff", bd=0, bg="#fff",
           command=lambda: next_button_clicked(email_entry.get(), password_entry.get())).place(x=350, y=380)

    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(applog, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)

    applog.mainloop()


def next_button_clicked(email, password):
    if not check_empty_fields(email, password):
        return

    # DATA BASE VALIDATION
    module()


def signup():
    """
       fonction qui permet de creer la page SignUp ou l'utilisateur doit s'inscrire en faisant
       entrer ses données personnelles
    """

    root.withdraw()
    global tk_image3
    appsign = Toplevel()
    # fct prec
    pages_stack.append(appsign)
    appsign.title("Sign Up")
    appsign.resizable(False, False)

    signUp_image = resize_image('page2_signup.jpg')
    signUp_label = Label(appsign, image=signUp_image)
    signUp_label.pack()
    frame1 = Frame(appsign, width=300, height=360, bg="#fff")
    frame1.place(x=105, y=140)

    # Creation de "entry widgets" avec un text par defaut
    global firstname, lastname, email, password
    firstname = create_entry(appsign, "firstname", 130, 120)
    lastname = create_entry(appsign, "lastname", 130, 200)
    email = create_entry(appsign, "email", 130, 280)
    password = create_entry(appsign, "password", 130, 360)

    # creation des frames qui soulignent les widgets
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=25)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=105)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=185)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=265)

    # creation du bouton "create"
    create_button_image = resize_image('create_button.jpg', (135, 80))
    Button(frame1, image=create_button_image, bd=0, activebackground="#fff", bg="#fff", command=create).place(x=60,
                                                                                                              y=294)

    # button precedent
    prec_image = resize_image('prec.jpg', (135, 80))
    Button(appsign, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)

    appsign.mainloop()


frame = Frame(root, width="200", height="200", bg="#fff")
frame.place(x=190, y=280)

# code pour login bouton
login_button_image = resize_image('loginbtn.jpg', (150, 80))
login_button = Button(frame, image=login_button_image, activebackground="#fff", bd=0, bg="#fff", command=login)
login_button.place(x=20, y=10)

# code pour signUp bouton
SignUp_button_image = resize_image('signupbtn.jpg', (150, 80))
signUp_button = Button(frame, image=SignUp_button_image, activebackground="#fff", bd=0, bg="#fff", command=signup)
signUp_button.place(x=20, y=100)

root.mainloop()