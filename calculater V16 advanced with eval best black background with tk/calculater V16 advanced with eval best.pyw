import os,sys
import tkinter as tk
s=open("a.txt","w+")
s.close()
t=open("b.txt","w+")
t.close()
def one():
      try:
            s=open("a.txt","a+")
            s.write('1')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def two():
      try:
            s=open("a.txt","a+")
            s.write('2')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def three():
      try:
            s=open("a.txt","a+")
            s.write('3')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def four():
      try:
            s=open("a.txt","a+")
            s.write('4')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def five():
      try:
            s=open("a.txt","a+")
            s.write('5')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def six():
      try:
            s=open("a.txt","a+")
            s.write('6')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def seven():
      try:
            s=open("a.txt","a+")
            s.write('7')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def eight():
      try:
            s=open("a.txt","a+")
            s.write('8')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def nine():
      try:
            s=open("a.txt","a+")
            s.write('9')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def zero():
      try:
            s=open("a.txt","a+")
            s.write('0')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def dot():
      try:
            s=open("a.txt","a+")
            s.write('.')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass

def dot1():
      try:
            s=open("a.txt","a+")
            s.write('(')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass

def dot2():
      try:
            s=open("a.txt","a+")
            s.write(')')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass



      
def clear():
      try:
            s=open("a.txt","w+")
            s.close()
            p=open("b.txt","w+")
            p.close()
            print("ALL MEMORY WAS CLEARED..")
            L2=tk.Label(root,text="ALL MEMORY WAS CLEARED..",bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            return
      except:
            pass
def plus():
      try:
            q=open("b.txt","r+")
            l=q.read()
            q.close()
            
            q=open("b.txt","w+")
            q.close()
            
            s=open("a.txt","a+")
            s.write(l)
            s.write('+')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def minus():
      try:
            q=open("b.txt","r+")
            l=q.read()
            q.close()

            q=open("b.txt","w+")
            q.close()
            
            s=open("a.txt","a+")
            s.write(l)
            s.write('-')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def multi():
      try:
            q=open("b.txt","r+")
            l=q.read()
            q.close()
            
            q=open("b.txt","w+")
            q.close()
            
            s=open("a.txt","a+")
            s.write(l)
            s.write('*')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def divid():
      try:
            q=open("b.txt","r+")
            l=q.read()
            q.close()
            
            q=open("b.txt","w+")
            q.close()
            
            s=open("a.txt","a+")
            s.write(l)
            s.write('/')
            s.close()
            a=open("a.txt","r")
            b=a.read()
            print(b)
            L2=tk.Label(root,text=b,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
            a.close()
            return
      except:
            pass
def eqal():
      try:
            q=open("a.txt","r+")
            l=q.read()
            q.close()
            lol=len(l)
            if lol==0:
                  pass
            else:
                  try:
                        ll=str(float(eval(l)))
                        if "e" in ll:
                              ll=("("+ll+")")
                        else:
                              pass
                  except:
                        print(".NOT A VALID CALCULATION.")
                        L2=tk.Label(root,text=".NOT A VALID CALCULATION.",bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)

                  q=open("a.txt","w+")
                  q.close()
                    
                  u=open("b.txt","w+")
                  u.write(ll)
                  u.close()
                  
                  lel=str(l+" = "+ll)
                  
                  print(lel)
                  L2=tk.Label(root,text=lel,bg='red',fg='white',font='bold').place(relx=0.34,rely=0.22,relwidth=0.54,relheight=0.14)
                  
      except:
            pass

root = tk.Tk()
root.geometry("1100x700+200+50")
root.title('BEST SIMPLE CALCULATER')
L1=tk.Label(root,text="'''''SIMPLE CALCULATER'''''",bg='red',fg='blue',font=('bold',18)).place(relx=0.354,rely=0.07)
onel = tk.Button(root, text="1",bg='red',fg='blue',font='bold', command=one,activeforeground="red",activebackground="black").place(relx=0.1,rely=0.35,relwidth=0.06,relheight=0.1)
one2 = tk.Button(root, text="2",bg='red',fg='blue',font='bold', command=two,activeforeground="red",activebackground="black").place(relx=0.17,rely=0.35,relwidth=0.06,relheight=0.1)
one3 = tk.Button(root, text="3",bg='red',fg='blue',font='bold', command=three,activeforeground="red",activebackground="black").place(relx=0.24,rely=0.35,relwidth=0.06,relheight=0.1)
one4 = tk.Button(root, text="4",bg='red',fg='blue',font='bold', command=four,activeforeground="red",activebackground="black").place(relx=0.1,rely=0.46,relwidth=0.06,relheight=0.1)
one5 = tk.Button(root, text="5",bg='red',fg='blue',font='bold', command=five,activeforeground="red",activebackground="black").place(relx=0.17,rely=0.46,relwidth=0.06,relheight=0.1)
one6 = tk.Button(root, text="6",bg='red',fg='blue',font='bold', command=six,activeforeground="red",activebackground="black").place(relx=0.24,rely=0.46,relwidth=0.06,relheight=0.1)
one7 = tk.Button(root, text="7",bg='red',fg='blue',font='bold', command=seven,activeforeground="red",activebackground="black").place(relx=0.1,rely=0.57,relwidth=0.06,relheight=0.1)
one8 = tk.Button(root, text="8",bg='red',fg='blue',font='bold', command=eight,activeforeground="red",activebackground="black").place(relx=0.17,rely=0.57,relwidth=0.06,relheight=0.1)
one9 = tk.Button(root, text="9",bg='red',fg='blue',font='bold', command=nine,activeforeground="red",activebackground="black").place(relx=0.24,rely=0.57,relwidth=0.06,relheight=0.1)
one0 = tk.Button(root, text="0",bg='red',fg='blue',font='bold', command=zero,activeforeground="red",activebackground="black").place(relx=0.17,rely=0.68,relwidth=0.06,relheight=0.1)
onep = tk.Button(root, text="+",bg='red',fg='blue',font='bold', command=plus,activeforeground="red",activebackground="black").place(relx=0.46,rely=0.44,relwidth=0.07,relheight=0.11)
onem = tk.Button(root, text="-",bg='red',fg='blue',font='bold', command=minus,activeforeground="red",activebackground="black").place(relx=0.54,rely=0.44,relwidth=0.07,relheight=0.11)
oneml = tk.Button(root, text="*",bg='red',fg='blue',font='bold', command=multi,activeforeground="red",activebackground="black").place(relx=0.46,rely=0.56,relwidth=0.07,relheight=0.11)
onede = tk.Button(root, text="/",bg='red',fg='blue',font='bold', command=divid,activeforeground="red",activebackground="black").place(relx=0.54,rely=0.56,relwidth=0.07,relheight=0.11)
oneeq = tk.Button(root, text="=",bg='white',fg='black',font='bold', command=eqal,activeforeground="red",activebackground="black").place(relx=0.50,rely=0.69,relwidth=0.07,relheight=0.11)
onecl = tk.Button(root, text="CLEAR all",bg='white',fg='black',font='bold', command=clear,activeforeground="red",activebackground="black").place(relx=0.62,rely=0.52,relwidth=0.09,relheight=0.07)
qui = tk.Button(root, text="'EXIT'",bg='white',fg='black',font='bold', command=sys.exit,activeforeground="red",activebackground="black").place(relx=0.8,rely=0.8,relwidth=0.09,relheight=0.07)
onedot = tk.Button(root, text=".",bg='red',fg='blue',font='bold', command=dot,activeforeground="red",activebackground="black").place(relx=0.24,rely=0.68,relwidth=0.06,relheight=0.1)
onedot = tk.Button(root, text="(",bg='red',fg='blue',font='bold', command=dot1,activeforeground="red",activebackground="black").place(relx=0.1,rely=0.68,relwidth=0.06,relheight=0.1)
onedot = tk.Button(root, text=")",bg='red',fg='blue',font='bold', command=dot2,activeforeground="red",activebackground="black").place(relx=0.31,rely=0.68,relwidth=0.06,relheight=0.1)
root.mainloop()
