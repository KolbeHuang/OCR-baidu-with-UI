import tkinter as tk
import tkinter.filedialog
import OCR_baidu

mode = "general"        # default mode is basic general mode
image_path = ""         # global variable to store the image path
result = ""             # global variable to store the recognition result


def get_path():
    """
    This function will obtain the path of the image opened.
    """
    global image_path
    image_path = tkinter.filedialog.askopenfilename()


def mode_set():
    """
    This function will set the global variable mode based on radio button.
    """
    global mode
    mode=var.get()


def recognition():
    """
    This function will make the recognition based on the given information.
    """
    global result, image_path, mode
    curr_id = id.get()
    curr_key1 = key1.get()
    curr_key2 = key2.get()
    result = OCR_baidu.ocr_analysis(image_path, curr_id, curr_key1, curr_key2, mode)
    text_result.delete(0.0, 'end')      # delete the previous results in the text block
    text_result.insert('insert', result)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("光学字符识别 OCR recogition")
    root.geometry("800x500")

    # set up all the labels 
    l_welcome = tk.Label(root, text='Welcome to Kolbe simple OCR!', font=("Arial", 18), height=2)    # set up label's feature
    l_welcome.pack()    # pin the label

    l_id = tk.Label(root, text='AppID', height=2)    
    l_id.pack()  

    l_key1 = tk.Label(root, text='API Key', height=2)    
    l_key1.pack()   

    l_key2 = tk.Label(root, text='Secret Key', height=2)    
    l_key2.pack()   

    l_id.place(relx=0.05, rely=0.1, relheight=0.05, relwidth=0.1)
    l_key1.place(relx=0.35, rely=0.1, relheight=0.05, relwidth=0.1)
    l_key2.place(relx=0.65, rely=0.1, relheight=0.05, relwidth=0.1)


    # create the buttons to choose the mode
    var=tk.StringVar()
    var.set("general")      # default

    # set up all the radio buttons 
    r1=tk.Radiobutton(root,text='基础模式 general',
                    variable=var,value='general',
                    command=mode_set)
    r1.pack()   # pin the button

    r2=tk.Radiobutton(root,text='高精度模式 acurate',
                    variable=var,value='accurate',
                    command=mode_set)
    r2.pack()

    r3=tk.Radiobutton(root,text='位置模式 location',
                    variable=var,value='location',
                    command=mode_set)
    r3.pack()

    r4=tk.Radiobutton(root,text='手写识别模式 handwritting',
                    variable=var,value='hand',
                    command=mode_set)
    r4.pack()

    r1.place(relx=0.05, rely=0.15, relheight=0.1, relwidth=0.2)
    r2.place(relx=0.25, rely=0.15, relheight=0.1, relwidth=0.2)
    r3.place(relx=0.45, rely=0.15, relheight=0.1, relwidth=0.2)
    r4.place(relx=0.65, rely=0.15, relheight=0.1, relwidth=0.25)


    # set up all the text windows
    # this is default infomation (my own id and keys)
    id = tk.StringVar()
    id.set('25194054')
    key1 = tk.StringVar()
    key1.set('frb7XgojpDGQmBGypaIXgDGP')
    key2 = tk.StringVar()
    key2.set('My5Ul4c76IF3hC4GeKGR9oVegqmrRBAV')

    e_id = tk.Entry(root, textvariable=id)
    e_id.pack()

    e_key1 = tk.Entry(root, textvariable=key1, show="*")
    e_key1.pack()

    e_key2 = tk.Entry(root, textvariable=key2, show="*")
    e_key2.pack()

    e_id.place(relx=0.15, rely=0.1, relheight=0.05, relwidth=0.1)
    e_key1.place(relx=0.45, rely=0.1, relheight=0.05, relwidth=0.1)
    e_key2.place(relx=0.75, rely=0.1, relheight=0.05, relwidth=0.1)


    # set up the convert button
    b_convert = tk.Button(root, text="识别 recognize", command=recognition)
    b_convert.pack()
    b_convert.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.15)


    # set up the menu bar
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Open', command=get_path)
    menu_bar.add_cascade(label='File', menu=file_menu)

    root.config(menu=menu_bar)


    # set up the text block for recognition output
    text_result = tk.Text(root)
    text_result.pack()
    text_result.place(relx=0.1, rely=0.25, relheight=0.6, relwidth=0.8)


    root.mainloop()