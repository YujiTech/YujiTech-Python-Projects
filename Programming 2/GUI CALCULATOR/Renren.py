from tkinter import *
def buttclick(numnchar):     #function to interpret commands

    if numnchar=="=":          #code evaluate numbers in the window
        p=r.get()
        r.delete(0,END)
        r.insert(0,eval(p))
    elif numnchar=='C':            #cancel command(C)
        r.delete(0,END)
    elif numnchar=='<-':           #backspace : r.delete(-1) wont work as it needs 2 args
        q=r.get()
        r.delete(0,END)
        r.insert(0,q[:-1])
    else:            
                    #used to show the expression
        curr = r.get()
        r.delete(0, END)
        r.insert(0, str(curr) + str(numnchar))


#root window and title
root=Tk()
root.title('simple calculatinator')



#gui
r=Entry(root,text='no val',width=40)
r.grid(column=0,row=0,columnspan=4,padx=10,pady=10)
#excuse the butt joke
butt1=Button(root,text='7',padx=40,pady=20,command=lambda:buttclick(7)).grid(row=1,column=0)
butt2=Button(root,text='8',padx=40,pady=20,command=lambda:buttclick(8)).grid(row=1,column=1)
butt3=Button(root,text='9',padx=40,pady=20,command=lambda:buttclick(9)).grid(row=1,column=2)
butt4=Button(root,text='4',padx=40,pady=20,command=lambda:buttclick(4)).grid(row=2,column=0)
butt5=Button(root,text='5',padx=40,pady=20,command=lambda:buttclick(5)).grid(row=2,column=1)
butt6=Button(root,text='6',padx=40,pady=20,command=lambda:buttclick(6)).grid(row=2,column=2)
butt7=Button(root,text='1',padx=40,pady=20,command=lambda:buttclick(1)).grid(row=3,column=0)
butt8=Button(root,text='2',padx=40,pady=20,command=lambda:buttclick(2)).grid(row=3,column=1)
butt9=Button(root,text='3',padx=40,pady=20,command=lambda:buttclick(3)).grid(row=3,column=2)
butt0=Button(root,text='0',padx=40,pady=20,command=lambda:buttclick('0')).grid(row=4,column=1)
buttmin=Button(root,text='-',padx=40,pady=20,command=lambda:buttclick('-')).grid(row=1,column=3)
buttadd=Button(root,text='+',padx=40,pady=20,command=lambda:buttclick('+')).grid(row=2,column=3)
buttmul=Button(root,text='x',padx=40,pady=20,command=lambda:buttclick('*')).grid(row=3,column=3)
buttdiv=Button(root,text='/',padx=40,pady=20,command=lambda:buttclick('/')).grid(row=4,column=2)
buttrem=Button(root,text='%',padx=40,pady=20,command=lambda:buttclick('%')).grid(row=4,column=0)
buttex=Button(root,text='exp',padx=40,pady=20,command=lambda:buttclick('**')).grid(row=4,column=3)
butteq=Button(root,text='=',padx=80,pady=20,command=lambda:buttclick('=')).grid(row=5,column=0,columnspan=3)
buttpoint=Button(root,text='.',padx=40,pady=20,command=lambda:buttclick('.')).grid(row=5,column=2)
buttclear=Button(root,text='C',padx=40,pady=20,command=lambda:buttclick('C')).grid(row=5,column=3)
buttback=Button(root,text='<-',padx=20,pady=10,command=lambda:buttclick('<-')).grid(row=0,column=3)
root.mainloop()

