from tkinter import *
from PIL import ImageTk, Image
from PIL import Image, ImageTk, ImageFilter
import sqlite3
import subprocess
import iagi
from tkinter import messagebox



pages_stack = []
# Permet l'accesibilite de root dans toute la page 
def container(r):
    global root
    root = r

def resize_image(image_path, size=(500, 500)):
    """
    Resizes the image found at image_path to the specified size.
    """
    
    original_image = Image.open(image_path)
    resized_image = original_image.resize(size)
    tk_image = ImageTk.PhotoImage(resized_image)
    return tk_image


# Define a function to clear the placeholder text
def on_enter(entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, 'end')
        entry_widget['fg'] = 'black'  # Change text color to black when the user clicks to enter data


# Define a function to insert the placeholder text if the field is empty
def on_leave(entry_widget, placeholder):
    if not entry_widget.get():
        entry_widget.insert(0, placeholder)
        entry_widget['fg'] = 'gray'  # Change text color back to gray for the placeholder text


def create_entry(appsign, default_text, x, y):
    entry = Entry(appsign, width=25, border=0, fg="gray", bg="#fff",
                  font=('Microsoft YaHei UI Light', 12, 'bold'))
    entry.insert(0, default_text)
    entry.bind('<FocusIn>', lambda e: on_enter(entry, default_text))
    entry.bind('<FocusOut>', lambda e: on_leave(entry, default_text))
    entry.place(x=x, y=y)
    return entry

def execute_sql(sql, data=None):
    
    try:
        if data is not None:
            iagi.curseur.execute(sql, data)
        else:
            iagi.curseur.execute(sql)
        iagi.connexion.commit()
        return True
    except Exception as e:
        messagebox.showerror('Erreur', f'Une erreur s\'est produite: {str(e)}')
        return False

def afficher():
    
    iagi.connexion.row_factory = sqlite3.Row
    iagi.curseur = iagi.connexion.execute("SELECT * FROM students")  # select all content
    for row in iagi.curseur:
        print(row["id"], row["firstname"], row["lastname"], row["email"])

#___________________________________________________________________________________
# fonction de validation

def verifier_utilisateur(email, mot_de_passe):
    iagi.curseur.execute('SELECT passwd FROM students WHERE email=?', (email,))
    result = iagi.curseur.fetchone()
    if result and result[0] == mot_de_passe:
        return 1
    else:
        return 0

def check_empty_fields(email_entry, password_entry):
    if not email_entry or not password_entry or email_entry=="email" or password_entry=="password":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return False

    return True

def on_submit(email_entry, password_entry):
    email = email_entry.get()
    mot_de_passe = password_entry.get()
    if not check_empty_fields(email, mot_de_passe):
        return 0
    if verifier_utilisateur(email, mot_de_passe):
        messagebox.showinfo("Connexion réussie", "Bienvenue, " + email)
        return 1
    else:
        messagebox.showerror("Erreur de connexion", "Email ou mot de passe incorrect")
        return 0
    
#______________________________________________________________________________________
# responsable a la suppression des utilisateurs
def delete(email_entry):
    iagi.curseur.execute('DELETE FROM students WHERE email=?', (email_entry,))
    iagi.connexion.commit()
    messagebox.showinfo("Succès", "Utilisateur supprimé avec succès")

def delete_user(email_entry):
    email_to_delete = email_entry.get()
    if email_to_delete:
        delete(email_to_delete)
        return 1
    else:
        messagebox.showwarning("Avertissement", "Veuillez fournir un email pour supprimer l'utilisateur.")
        return 0
#____________________________________________________________________________________________
# button precedent 

def prec():
    global root, pages_stack
    # Function to go back to the previous page
    if pages_stack:
        current_page = pages_stack.pop()
        current_page.withdraw()
        if pages_stack:
            previous_page = pages_stack[-1]
            previous_page.deiconify()
        else:
            root.deiconify()

#___________________________________________________________________________________________
# Partie Module qui permet d'afficher les modules disponibles

def ouvrir_pdf_avec_chrome(pdf_path):
    # Utiliser subprocess pour ouvrir Google Chrome avec le fichier PDF
    subprocess.Popen(["start", "", pdf_path], shell=True)

def back_to_welcome():
    for page in pages_stack:
        page.withdraw()
    root.deiconify()
    
btnstate=False   
def barre(nav, tk_image3, closebtn, F1, F2, F3):
    global btnstate

    if btnstate is True:
        #create animated navbar closing
        for x in range(0,201,10):
            nav.place(x=-x,y=0)
            tk_image3.update()


        btnstate=False
        closebtn.place_forget()
        F1.place_forget()
        F2.place_forget()
        F3.place_forget()

    else:
        for x in range(-300,0):
            nav.place(x=x,y=0)
            tk_image3.update()
        btnstate=True
        # Show the close_image button when the nav is open
        closebtn.place(x=0,y=440)
        F1.place(x=15,y=150)
        F2.place(x=15,y=250)
        F3.place(x=15, y=350)

def open_subject(title, image_name, pdf_files,tk_image5):
    tk_image5.withdraw()
    global tk_subject
    subject = Toplevel()
    pages_stack.append(subject)
    tk_subject = subject
    subject.title(title)
    subject.resizable(False, False)

    subject_arriere = resize_image(image_name)
    subject_label = Label(subject, image=subject_arriere)
    subject_label.pack()

    # Button precedent
    prec_image = resize_image('images/prec.jpg', (135, 80))
    Button(tk_subject, image=prec_image, activebackground="#fff", bd=0, bg="#fff", command=prec).place(x=350, y=100)
    
    chap1 = resize_image('images/chap1.jpg', (340, 40))
    Button(tk_subject, image=chap1, bd=0,activebackground="#fff", bg="#fff",command=lambda:ouvrir_pdf_avec_chrome(pdf_files[0])).place(x=75, y=180)
    chap2 = resize_image('images/chap2.jpg', (340, 40))
    Button(tk_subject, image=chap2, bd=0,activebackground="#fff", bg="#fff",command=lambda:ouvrir_pdf_avec_chrome(pdf_files[1])).place(x=85, y=260)
    chap3 = resize_image('images/chap3.jpg', (320, 40))
    Button(tk_subject, image=chap3, bd=0,activebackground="#fff", bg="#fff",command=lambda:ouvrir_pdf_avec_chrome(pdf_files[2])).place(x=80, y=340)
    
        #button pour la barre
    bar_image=resize_image('images/barre.jpg',(65,65))
    Button(subject, image=bar_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:barre(nav, tk_image3, closebtn, F1, F2, F3)).place(x=0,y=440)

    #setting du barre
    global nav
    nav = Frame(subject, bg="#042F69", height=600, width=200)
    nav.place(x=-200, y=0)
    
    global F1,F2,F3
    F1=Frame(nav, width=170, height=1, bg="#EFB054")
    F2=Frame(nav, width=170, height=1, bg="#EFB054")
    F3 = Frame(nav, width=170, height=1, bg="#EFB054")

    Button(nav, text="les modules", font=('Microsoft YaHei UI Light',15,'bold'),bd=0,
           bg="#042F69", fg="#fff", activebackground="#042F69", activeforeground="gray17", command=lambda:module).place(x=25,y=100)
    # button qui retourne vers la première page
    Button(nav, text="log out", font=('Microsoft YaHei UI Light',15,'bold'),bd=0,
           bg="#042F69", fg="#fff", command=back_to_welcome).place(x=25, y=200)
    # button qui supprime l'utilisateur de la base de donnee
    Button(nav, text="supprimer l'identifiant", font=('Microsoft YaHei UI Light',10,'bold'),bd=0,
           bg="#042F69", fg="#fff", command=lambda:delete_user(email_entry)).place(x=25, y=300)
    global closebtn
    close_image = resize_image('images/close_bar.jpg', (65, 65))
    closebtn=Button(subject, image=close_image,activebackground="#042F69" ,bd=0, bg="#042F69", command=lambda:barre(nav, tk_image3, closebtn, F1, F2, F3))

    subject.mainloop()


# Des fonctions qui permettent l'ouverture de la page des chapitres
def oop(tk_image5):
    open_subject("OOP/python", 'images/python.jpg', ["cours/Chapitre 5 - Héritage (1).pdf", "cours/Chapitre 6 - Gestion des fichiers.pdf", "cours/Base de données chap8.pdf"],tk_image5)

def ro(tk_image5):
    open_subject("R.O", 'images/RO_ar.jpg', ["cours/01-Introduction_RO.pdf", "cours/02-Prog Lineaire - ROPart1.pdf", "cours/02-Prog Lineaire - ROPart2.pdf"],tk_image5)

def sdd(tk_image5):
    open_subject("SDD", 'images/sdd_ar.jpg', ["cours/Structure de données en C - Seance 0 - complexite.pdf", "cours/Structure de données en C - Seance 1 - Listes chainées .pdf", "cours/Structure de données en C - Seance 2 - Listes chainées .pdf"],tk_image5)

def linux(tk_image5):
    open_subject("Linux", 'images/linx_ar.jpg', ["cours/Systèmes d_exploitation - chap 1 - Introduction UNIX- LINUX.pdf", "cours/Systèmes d_exploitation - chap 2 - la gestion de fichier sous linux.pdf", "cours/Systèmes d_exploitation - chap 3 - gestion des utilisateurs et des groupes.pdf"],tk_image5)

def module(tk_image3):
    
    tk_image3.withdraw()
    global tk_image5
    modules = Toplevel()
    pages_stack.append(modules)
    tk_image5=modules
    modules.title("IAGI-1")
    modules.resizable(False, False)

    iagi_image = resize_image('images/IAGI.png')
    iagi_label = Label(modules, image=iagi_image )
    iagi_label.pack()

    frame2 = Frame(modules, width=290, height=300, bg="#fff")
    frame2.place(x=105, y=180)
    
    python_image = resize_image('images/oop.jpg', (250, 40))
    Button(modules, image=python_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:oop(tk_image5)).place(x=110, y=200)

    ro_image = resize_image('images/RO.jpg', (320, 40))
    Button(modules, image=ro_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:ro(tk_image5)).place(x=110, y=270)

    linux_image = resize_image('images/linux.jpg', (250, 40))
    Button(modules, image=linux_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:linux(tk_image5)).place(x=110, y=340)

    sdd_image = resize_image('images/sdd.jpg', (320, 40))
    Button(modules, image=sdd_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:sdd(tk_image5)).place(x=110, y=410)

    #button pour la barre
    bar_image=resize_image('images/barre.jpg',(65,65))
    Button(modules, image=bar_image, bd=0, bg="#fff",activebackground="#fff",command=lambda:barre(nav, tk_image3, closebtn, F1, F2, F3)).place(x=0,y=440)

    #setting du barre
    global nav
    nav = Frame(modules, bg="#042F69", height=600, width=200)
    nav.place(x=-200, y=0)
    
    global F1,F2,F3
    F1=Frame(nav, width=170, height=1, bg="#EFB054")
    F2=Frame(nav, width=170, height=1, bg="#EFB054")
    F3 = Frame(nav, width=170, height=1, bg="#EFB054")

    Button(nav, text="les modules", font=('Microsoft YaHei UI Light',15,'bold'),bd=0,
           bg="#042F69", fg="#fff", activebackground="#042F69", activeforeground="gray17", command=lambda:module).place(x=25,y=100)
    # button qui retourne vers la première page
    Button(nav, text="log out", font=('Microsoft YaHei UI Light',15,'bold'),bd=0,
           bg="#042F69", fg="#fff", command=back_to_welcome).place(x=25, y=200)
    # button qui supprime l'utilisateur de la base de donnee
    Button(nav, text="supprimer l'identifiant", font=('Microsoft YaHei UI Light',10,'bold'),bd=0,
           bg="#042F69", fg="#fff", command=lambda:delete_user(email_entry)).place(x=25, y=300)
    global closebtn
    close_image = resize_image('images/close_bar.jpg', (65, 65))
    closebtn=Button(modules, image=close_image,activebackground="#042F69" ,bd=0, bg="#042F69", command=lambda:barre(nav, tk_image3, closebtn, F1, F2, F3))

    prec_image = resize_image('images/prec.jpg', (135, 80))
    Button(modules , image=prec_image, bd=0,activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)
    modules.mainloop()

#___________________________________________________________________________________________
# Partie Log in 

def log_next(email_entry, password_entry, tk_image3):
    check_empty_fields(email_entry, password_entry)
    if on_submit(email_entry, password_entry) == 1:
        module(tk_image3)
    else:
        return

def login(root):
    global tk_image3
    root.withdraw()
    applog = Toplevel()
    pages_stack.append(applog)
    tk_image3 = applog
    applog.title("Log In")
    applog.resizable(False, False)
    applog.wm_title("applog")

    login_image = resize_image('images/page2_login.jpg')
    login_label = Label(applog, image=login_image)
    login_label.pack()
    frame2 = Frame(applog, width=300, height=360, bg="#fff")
    frame2.place(x=105, y=120)

    global email_entry
    email_entry = create_entry(applog, "email", 130, 200)
    global password_entry
    password_entry = create_entry(applog, "password", 130, 280)
    
    Frame(frame2, width=260, height=1, bg="#004aad").place(x=7, y=110)
    Frame(frame2, width=260, height=1, bg="#004aad").place(x=7, y=190)

    next_button_image = resize_image('images/next_button.jpg', (135, 80))
    Button(applog, image=next_button_image, activebackground="#fff", bd=0, bg="#fff", command=lambda:log_next(email_entry, password_entry,tk_image3)).place(x=350, y=380)

    prec_image = resize_image('images/prec.jpg', (135, 80))
    Button(applog, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)

    applog.mainloop()

#___________________________________________________________________________________________
# Partie Sign Up

def create(firstname, lastname, email, password):
    
    sql = "INSERT INTO STUDENTS (firstname, lastname, email, passwd) VALUES (?, ?, ?, ?)"
    data = (firstname.get(), lastname.get(), email.get(), password.get())
    if execute_sql(sql, data):
        messagebox.showinfo('message', 'Done!')
        return True
    return False

def sign_next(firstname, lastname, email, password, tk_image3):
    if create(firstname, lastname, email, password) == 1:
        module(tk_image3)
    else:
        return

def signup(root):
    global tk_image3
    root.withdraw()
    appsign = Toplevel()
    pages_stack.append(appsign)
    tk_image3 = appsign
    appsign.title("Sign Up")
    appsign.resizable(False, False)
    appsign.wm_title("appsign")

    signUp_image = resize_image('images/page2_signup.jpg')
    signUp_label = Label(appsign, image=signUp_image)
    signUp_label.pack()
    frame1 = Frame(appsign, width=300, height=360, bg="#fff")
    frame1.place(x=105, y=140)

    global firstname, lastname, email, password
    firstname = create_entry(appsign, "firstname", 130, 120)
    lastname = create_entry(appsign, "lastname", 130, 200)
    email = create_entry(appsign, "email", 130, 280)
    password = create_entry(appsign, "password", 130, 360)

    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=25)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=105)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=185)
    Frame(frame1, width=260, height=1, bg="#004aad").place(x=7, y=265)

    create_button_image = resize_image('images/create_button.jpg', (135, 80))
    Button(frame1, image=create_button_image, bd=0, activebackground="#fff", bg="#fff", command=lambda:sign_next(firstname, lastname, email, password, tk_image3)).place(x=60, y=294)

    prec_image = resize_image('images/prec.jpg', (135, 80))
    Button(appsign, image=prec_image, bd=0, activebackground="#fff", bg="#fff", command=prec).place(x=350, y=100)

    appsign.mainloop()