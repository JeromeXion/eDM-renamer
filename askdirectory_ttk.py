import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import zipfile


def selectEDMRfile(): 
    path =filedialog.askdirectory()
    print(path)
    ttk.text1.insert(INSERT,path)

def CloseThisWindow():
    root.destroy()

def MkdirProcess():
    if (ttk.text1.get() and ttk.PCA_MPN.get() and ttk.PCB_MPN.get()):
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA")
        md(ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB")
        md(ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-A-STCL "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-FABD "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-ODBP "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-PHOT "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-ADWG "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-REFD "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-SCHM "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-SPEC "+ttk.VER.get())
        md(ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-C-CONT "+ttk.VER.get())
        messagebox.showinfo(title="Create",message="Folders create successful, Please go to step 2")
    else:
        messagebox.showerror(title="Error",message="Please fill all blanks")

def ReAssemble():

    #STCL : Gerber file, zip and rename.
    path_stcl = ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-A-STCL "+ttk.VER.get()
    filename_stcl = ttk.PCB_MPN.get()+"-A-STCL"
    pyzip(path_stcl,filename_stcl)
    
    # FABD : Drill file, zip and rename.
    path_fabd = ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-FABD "+ttk.VER.get()
    filename_fabd = ttk.PCB_MPN.get()+"-B-FABD"
    pyzip(path_stcl,filename_fabd)

    # ODBP : ODB++ file: zip and rename
    path_odbp = ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-ODBP "+ttk.VER.get()
    filename_odbp = ttk.PCB_MPN.get()+"-B-ODBP"
    pyzip(path_odbp,filename_odbp)

    # PHOT : PCB file: rename
    path_phot = ttk.text1.get()+"/"+ttk.PCB_MPN.get()+" PCB/"+ttk.PCB_MPN.get()+"-B-PHOT "+ttk.VER.get()
    filename_phot = ttk.PCB_MPN.get()+"-B-PHOT"
    pyzip(path_phot,filename_phot)
    
    # ADWG : silk print file: rename
    path_adwg = ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-ADWG "+ttk.VER.get()
    filename_adwg = ttk.PCA_MPN.get()+"-A-ADWG"
    pyzip(path_adwg,filename_adwg)

    # REFD : BOM file: rename
    path_refd = ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-REFD "+ttk.VER.get()
    filename_refd = ttk.PCA_MPN.get()+"-A-REFD"
    pyzip(path_refd,filename_refd)

    # SCHM : Schematic file: rename
    path_schm = ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-SCHM "+ttk.VER.get()
    filename_schm = ttk.PCA_MPN.get()+"-A-SCHM"
    pyzip(path_schm,filename_schm)

    # SPEC : PCA specification : rename
    path_spec = ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-A-SPEC "+ttk.VER.get()
    filename_spec = ttk.PCA_MPN.get()+"-A-SPEC"
    #rename(path_spec,filename_spec)
    pyzip(path_spec,filename_spec)

    # CONT : Schematic source file: zip and rename
    path_cont = ttk.text1.get()+"/"+ttk.PCA_MPN.get()+" PCA/"+ttk.PCA_MPN.get()+"-C-CONT "+ttk.VER.get()
    filename_cont = ttk.PCA_MPN.get()+"-C-CONT"
    pyzip(path_cont,filename_cont)
    # Zip done messagebox
    messagebox.showinfo(title="Package done",message="Package Done!")

    
def md(path):
    print('make dir:%s' %path)
    if not os.path.exists(path):
        # only one layer of directory
        os.makedirs(path)

def rename(path, newFilename):
    #print("当前目录:",path)
    file_list = os.listdir(path)
    #print("文件列表",file_list) 
    for file in file_list:        
        old_dir = os.path.join(path,file)          
        filename = os.path.splitext(file)[0]
        #print("文件名称",filename)
        filetype = os.path.splitext(file)[1]
        #print("文件类型",filetype)
        old_name = filename + filetype
        #print("old name is:", old_name)
        new_name = newFilename
        #print("new name is:", new_name)
        new_dir = os.path.join(path, new_name + filetype)  # new path+filetype
        os.rename(old_dir, new_dir)  				 
        # print("DONE")     
        if os.path.isdir(new_dir):
            rename(new_dir)

def pyzip(filepath,archive_name):
    os.chdir( os.path.dirname(filepath))
    f = zipfile.ZipFile(archive_name+".zip",'w',zipfile.ZIP_DEFLATED)
    os.chdir( filepath )
    startdir = filepath
    for dirpath,dirnames,filenames in os.walk(startdir):
        for filename in filenames:
            #f.write(os.path.join(dirpath,filename))
            f.write(os.path.join('.',filename))
            # messagebox.showinfo(title="Package done",message="Package Done!")
    
    #print("压缩完成，目录：",startdir)
    f.close()
 
if __name__=="__main__":
    
    root=Tk() 
	
    #ttk object
    tabControl = ttk.Notebook(root)

    #set title
    root.title('eDMR PCB/PCA Files Packaging Tool')

    #Set window size and position
    root.geometry('500x300+570+200')

    #Add tab1 create folder
    tab1= ttk.Frame(tabControl)# Create a tab
    tabControl.add(tab1, text='Step 1：Create folders')# Add the tab 1
    tabControl.grid(column=0, row=0)
    
    #Add tab2 zip
    tab2= ttk.Frame(tabControl)# Create a tab
    tabControl.add(tab2, text='Step 2: Package')# Add the tab 2
    
    #Add label
    ttk.label1 = Label(tab1,text='Select Path:')
    ttk.label2 = Label(tab1,text='PCA MPN:')
    ttk.label3 = Label(tab1,text='PCB MPN:')
    ttk.label4 = Label(tab1,text='Rev :')
    ttk.label5 = Label(tab2,text = 'Please put files into created folder and press package button')
    
    #Add text for folder path
    ttk.text1 = Entry(tab1,bg='white',width=40)
    # Add button commands
    ttk.button1 = Button(tab1,text='Browse',width=8,command=selectEDMRfile)
    ttk.button2 = Button(tab1,text='Create',width=8,command=MkdirProcess)
    ttk.button3 = Button(tab1,text='Exit',width=8,command=CloseThisWindow)
    ttk.button4 = Button(tab2,text='Package',width=8,command=ReAssemble)
    ttk.button5 = Button(tab2,text='Exit',width=8,command=CloseThisWindow)
    # Add Entry 
    ttk.PCA_MPN = Entry(tab1,width=40,bg="white",fg="black")
    ttk.PCB_MPN = Entry(tab1,width=40,bg="white",fg="black")
    ttk.VER = Entry(tab1,width=40,bg="white",fg="black")

    #  pack to make visable
    tabControl.pack(expand=1,fill="both")
    #  ttk placement  
    ttk.label1.place(x=30,y=30)
    ttk.text1.place(x=120,y=30)
    ttk.button1.place(x=390,y=26)
    ttk.button2.place(x=120,y=190)
    ttk.button3.place(x=360,y=190)
    ttk.button4.place(x=120,y=190)
    ttk.button5.place(x=360,y=190)
    ttk.label2.place(x=30,y=110)
    ttk.label3.place(x=30,y=150)
    ttk.label4.place(x=30,y=70)
    ttk.PCA_MPN.place(x=150,y=110)
    ttk.PCB_MPN.place(x=150,y=150)
    ttk.VER.place(x=150,y=70)
    ttk.label5.place(x=60,y=110)
 
    root.mainloop() 

    
