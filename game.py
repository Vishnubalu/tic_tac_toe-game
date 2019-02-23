import tkinter as tk
import os
import random
import time

class info:
    
    file = "none"
    name = "none"
    score = "0"
    total = "0"
    highest = "0"


def image_show():

    def home():
        root.destroy()
        Home()

    def Refresh():
        root.destroy()
        image_show()
        return
    
# To validate input and for message boxes
    def act():
        info.total = str(int(info.total)+1)
        
        def checkbutton():
            c=0
            v=0
            for name in enable:
                if(enable[name].get() in arr2[:5]):
                    print(enable[name].get())
                    c=c+1
                elif(enable[name].get()):
                    v = v+1
            if(c+v > 5):
                tk.messagebox.showerror("Error", "You cannot select more than 5 objects")
            else:
                c=c*20
                #tk.messagebox.showinfo("Say Hello", "Hello World")
                ans = list(map(lambda x:str(arr2.index(x)+1)+".  "+x[:-4] , arr2[:5]))
                tk.messagebox.showinfo("Congrats!", "Your score is : "+str(c)+"\n")
                info.score = str(int(info.score)+c)
                info.highest = info.score
                tk.messagebox.showinfo("Answers ", "\n".join(ans))
                f = open("vishnu.txt", "r").readlines()
                count = 0
                for line in f:
                    f_user, f_password, total, score = line.split(" ")
                    if(info.name == f_user):
                        f[count] = f_user+" "+f_password+" " +info.total+" "+info.score+"\n"
                        open('vishnu.txt', 'w').write(''.join(f))
                        #print(f)
                        break
                    count = count+1
                f = open("score.txt", "r").readlines()
                #print(f)
                if(int(f[0]) < int(info.highest)):
                    f[0] = info.highest
                    f[1] = f_user+" "+f_password+" " +info.total+" "+info.score
                    open('score.txt', 'w').write('\n'.join(f))
                root1.destroy()
                image_show()


# To create check boxes and submit button
        def quit():
            root.destroy()
            
        quit()
        import tkinter as tk
        root1=tk.Tk()
        root1.geometry("+{}+{}".format(500, 100))
        arr2 = []
        for item in arr:
            arr2.append(item)
        print(arr2)
        random.shuffle(arr)
        enable = {key: 0 for key in arr}
        for name in enable:
            enable[name] = tk.Variable()
            C1=tk.Checkbutton(root1,text=name[:-4],variable = enable[name],onvalue=name,offvalue=0
                       ,height=1,width=50, pady=10,bg = "lightblue")
            C1.pack()
        button=tk.Button(text="Submit", bg="green", pady=5, command=checkbutton)
        button.pack(pady=10)
        root1.mainloop()
    # Need to create a folder by the name game contains folders animals, fruits, vegetables and display_pics
    # In  which those should contain respective images (.png) saved with their names perfectly
    path = "/home/vishnubalu/Desktop/PROGRAMMING/Python/Python/python/python/game/"+info.file
    arr = os.listdir(path)
    arr = random.sample(arr[1:], 10)
    root=tk.Tk()
    root.geometry("+{}+{}".format(0, 0))
    root.title(17*"\t"+"VB LEARNING")
    frame1=tk.Frame(root,height=80,width=400)
    frame1.pack()
    canvas=tk.Canvas(frame1,width=1300,height=710,bg="grey")
    canvas.pack(expand="no",fill="both")
    img1=tk.PhotoImage(file=path+'/'+arr[0])
    canvas.create_image(0,0,image=img1,anchor="nw")
    img2=tk.PhotoImage(file=path+'/'+arr[1])
    canvas.create_image(950,0,image=img2,anchor="nw")
    img3=tk.PhotoImage(file=path+'/'+arr[2])
    canvas.create_image(500,130,image=img3,anchor="nw")
    img4=tk.PhotoImage(file=path+'/'+arr[3])
    canvas.create_image(10,330,image=img4,anchor="nw")
    img5=tk.PhotoImage(file=path+'/'+arr[4])
    canvas.create_image(950,330,image=img5,anchor="nw")
    button1=tk.Button(canvas, text="HOME", bg="lightblue", pady="5", command = home).place(x=450, y=650)
    button1 = tk.Button(canvas,  text = "REFRESH", bg = "lightblue", command = Refresh).place(x=650, y=650)
    button2=tk.Button(canvas, text="GUESS", bg="lightblue", pady="5", command=act).place(x=850, y=650)
    root.mainloop()

# To show the score card
def score_card():
    def call_home():
        hehe.destroy()
        Home()
    hehe = tk.Tk()
    hehe.title(10*"\t"+"PROFILE")
    hehe.geometry("+{}+{}".format(280,150))
    frame = tk.Frame(hehe, width = 700, height=500)
    frame.pack()
    canvas = tk.Canvas(frame, width = 800, height = 450, bg="grey")
    canvas.pack()
    f = open("score.txt", "r").readlines()
    allinfo = list(f[1].split(" "))
    #we need to give the file path for the display_pics
    path = "/home/vishnubalu/Desktop/PROGRAMMING/Python/Python/python/python/game/display_pics"
    arr = os.listdir(path)
    name = random.sample(arr, 1)
    img=tk.PhotoImage(file=path+"/"+name[0])
    canvas.create_image(10,10,image=img,anchor="nw")
    if(int(info.total) == 0):
        canvas.create_text(540, 30, text ="Hello "+ info.name, font = ('Helvetica',30, 'bold'), fill='red')
        canvas.create_text(560, 100, text ="EMPTY ", font = ('Helvetica',50, 'bold'), fill='red')
    else:
        canvas.create_text(540, 30, text ="Hello "+ info.name, font = ('Helvetica',30, 'bold'), fill='red')
        canvas.create_text(540, 80, text ="Total Score : "+ info.score, font = ('Helvetica', 20, 'bold'), fill='green')
        canvas.create_text(540, 120, text ="Total Games Played : "+ info.total, font = ('Helvetica', 20, 'bold'), fill='green')
        canvas.create_text(540, 150, text =" Accuracy : "+ str((int(info.score)/20)/int(info.total)*100/5)+"%", font = ('Helvetica', 20, 'bold'), fill='green')
    canvas.create_text(540, 220, text ="Highest Scorer : "+ allinfo[0], font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 270, text ="Total Score : "+ f[0], font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 320, text ="Total Games Played : "+ allinfo[2], font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 370, text =" Accuracy : "+ str((int(f[0])/20)/int(allinfo[2])*100/5)+"%", font = ('Helvetica', 20, 'bold'), fill='black')
    button = tk.Button(canvas, text = "OK", bg = "lightblue", command = call_home).place(x = 540, y=400)
    hehe.mainloop()

def Home():
    select = tk.Tk()
    select.title(100*" "+"HOME")
    select.geometry("+{}+{}".format(200, 70))
    frame = tk.Frame(select, height=1000, width = 600)
    frame.pack()
    canvas=tk.Canvas(frame, width=1000, height=600, bg="grey")
    canvas.pack(expand="no", fill="both")
    img = tk.PhotoImage(file = "fruit.png")
    canvas.create_image(10, 50, image=img, anchor="nw")
    gif2=tk.PhotoImage(file="vegetable.png")
    canvas.create_image(670, 50, image=gif2, anchor="nw")
    gif3=tk.PhotoImage(file="arctic_fox.png")
    canvas.create_image(350, 100, image=gif3, anchor="nw")
    
    def animals():
        info.file = "animals"
        select.destroy()
        image_show()
        
    def fruits():
        info.file = "fruits"
        select.destroy()
        image_show()
        
    def vegetables():
        info.file = "vegetables"
        select.destroy()
        image_show()
        
    def profile():
        select.destroy()
        score_card()
        
    def quit():
        result = tk.messagebox.askquestion("Delete", "Are You Sure?", icon='question')
        if result == 'yes':
            select.destroy()
        else:
            print("continue")

    button1 = tk.Button(canvas,  text = "Quit", bg = "lightblue", command = quit).place(x=295, y=10)
    button1 = tk.Button(canvas,  text = "FRUITS", bg = "lightblue", command = fruits).place(x=120, y= 550)
    button2 = tk.Button(canvas,  text = "ANIMALS", bg = "lightblue", command = animals).place(x=475, y=550)
    button3 = tk.Button(canvas,  text = "VEGETABLES", bg = "lightblue", command = vegetables).place(x=865, y=550)
    button4 = tk.Button(canvas,  text = "Profile", bg = "lightblue", command = profile).place(x=670, y=10)
    select.mainloop()

def login():
    user = e1.get()
    password = e2.get()
    f = open("vishnu.txt", "r").readlines()
    if(user == "" or password == ""):
        tk.messagebox.showinfo("Error", "Fields Should not be Empty")
    else:
        for line in f:
            f_user, f_password, total, score= line.split(" ")
            if(user == f_user and password == f_password):
                tk.messagebox.showinfo("WELL COME", "Successflly Logged In")
                info.total = total
                info.name = user
                info.score = score
                login_page.destroy()
                start()
                break
        else:
            tk.messagebox.showerror("ERROR!", "Incorrect User name or password")

def forgot():
    f = open("vishnu.txt", "r").readlines()
    user = e1.get()
    if(user == ""):
        tk.messagebox.showerror("Error", "User Name Field Should not be Empty")
    else:
        for line in f:
            f_user, f_password, total, score = line.split(" ")
            if(user == f_user):
                #label.config(text = f_password)
                tk.messagebox.showinfo("Remember", "Your Password : "+f_password)
                break
        else:
            tk.messagebox.showerror("ERROR!", "User Name Not Found")
            
def signup():
    user = e1.get()
    password = e2.get()
    f = open("vishnu.txt", "r").readlines()
    if(user == "" or password == ""):
        tk.messagebox.showerror("Error", "Fields Should not be Empty")
    else:
        for line in f:
            f_user, f_password, total, score = line.split(" ")
            if(user == f_user or password == f_password):
                tk.messagebox.showerror("Error", "User name or Password \n\n Already Exist")
                break
        else:
            f = open("vishnu.txt", "a")
            f.write(user+" "+password+" " +"0"+" "+"0\n")
            f.close()
            tk.messagebox.showinfo("Message", "Succussfully Signed Up \n\n\nLogin with same now!")

def Guide():
    tk.messagebox.showinfo("Information", "1. If you are New user, You need to SIGNUP first and then Login \n2. If you Forgot your password : type your username and hit fogot password \n ** Don't leave any field blank while Singup or Login**")

def start():

    def call_Home():
        start.destroy()
        Home()

    def quit():
        result = tk.messagebox.askquestion("Delete", "Are You Sure?", icon='question')
        if result == 'yes':
            start.destroy()
        else:
            print("continue")
            
    start = tk.Tk()
    start.geometry("+{}+{}".format(200,75))
    start.title(10*"\t"+"WELLCOME")
    frame = tk.Frame(start, height = 600, width = 1000, bg = "green")
    frame.pack()
    canvas=tk.Canvas(frame, width=1000, height=600, bg="grey")
    canvas.pack(expand="no",fill="both")
    img = tk.PhotoImage(file = "Child.png")
    canvas.create_image(200, 150, image=img, anchor="nw")
    canvas.create_text(540, 50, text = 'WELCOME TO', font = ('Helvetica', 50, 'bold'), justify = 'center', fill='lightblue')
    canvas.create_text(550, 120, text = 'VB LEARNING', font = ('Helvetica', 40, 'bold'), justify = 'center', fill='red')
    tk.Button(canvas,text = "START", bg="lightblue", command = call_Home).place(x = 550, y = 450)
    tk.Button(canvas,text = "QUIT", bg="tomato", command = quit).place(x = 400, y = 450)
    start.mainloop()

# LOGIN PAGE
login_page = tk.Tk()
login_page.geometry("+{}+{}".format(450,150))
login_page.title(3*"\t"+"WELLCOME")
Login = tk.Button(login_page, text = "Login", bg="lightblue", command = login).grid(row=5, column=4, padx=6, pady = 20)
Forgot = tk.Button(login_page, text = "Forgot Password", bg = "lightblue",command = forgot).grid(row=5, column=3, padx=6, pady = 20)
Signup = tk.Button(login_page, text = "Sign up", bg = "lightblue",command = signup).grid(row=0, column=4, padx=6, pady = 20)
guide = tk.Button(login_page, text = "Guide", bg = "lightblue",command = Guide).grid(row=0, column=1, padx=6, pady = 20)
tk.messagebox.showinfo("WELL COME", "You Must LogIn To Enter Into Game")
l1 = tk.Label(login_page, text = "User Name",height=5).grid(row=3, column=3, padx=20, pady = 10)
e1 = tk.Entry(login_page, bd=5)
l2 = tk.Label(login_page, text = "Password").grid(row=4, column=3, padx=20, pady = 10)
e2 = tk.Entry(login_page, bd=5)
e1.grid(row=3, column=4, padx=20, pady = 10)
e2.grid(row=4, column=4, padx=20, pady = 10)
label = tk.Label(login_page)
label.grid()
login_page.mainloop()









