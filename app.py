from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("Download Youtube")

def select_path_save_to():
    folder_selected = filedialog.askdirectory()
    input_saveto.insert(0, folder_selected)

def start_download():
    try:
        if input_url.get() == "":
            show_warning_not_insert_url()
        elif input_saveto.get() == "":
            show_warning_not_insert_path_save()
        else:
            print(input_url.get())
            print(input_saveto.get())
            link = input_url.get()
            video = YouTube(link)
            stream = video.streams.get_audio_only()
            stream.download(output_path=input_saveto.get())
            show_info_download_done()
            input_url.delete(0,1000)
    except:
        show_error_unknow()

def show_warning_not_insert_url():
    Tk().withdraw()
    messagebox.showwarning("Warning", "Please insert URL for download")

def show_warning_not_insert_path_save():
    Tk().withdraw()
    messagebox.showwarning("Warning", "Please select Path for save")

def show_error_unknow():
    Tk().withdraw()
    messagebox.showerror("Error", "Please re-check URL and Path")
    
def show_info_download_done():
    Tk().withdraw()
    messagebox.showinfo("Information", "Download completed")

label_url = Label(root, text="URL :")
label_url.grid(row=0, column=0, padx=5, pady=5)

label_saveto = Label(root, text="Save to :")
label_saveto.grid(row=1, column=0, padx=5, pady=5)

input_url = Entry(root, width=50)
input_url.grid(row=0, column=1, padx=5, pady=5)

input_saveto = Entry(root, width=50)
input_saveto.grid(row=1, column=1, padx=5, pady=5)

button_select_path = Button(root, text="...", width=4, command=select_path_save_to)
button_select_path.grid(row=1, column=2, padx=5, pady=5)

button = Button(root, text="Download", command=lambda:start_download())
button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()