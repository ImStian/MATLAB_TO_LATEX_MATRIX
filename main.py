from tkinter import *
import customtkinter

def generate_matrix(text):
    latex_code = r'$\begin{bmatrix} ' + '\n'
    text = text.strip('[]')
    rows = text.split(';')
    for row in rows:
        latex_code += str(row.replace(r',',r' & ')) + r'\\' + '\n'

    latex_code += r'\end{bmatrix}$'
    return latex_code



# apparence settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# creating window
root = customtkinter.CTk()
root.title('Latex Matrix generator')


# setting window width + height
root.geometry('300x325')

# adding label
label = customtkinter.CTkLabel(master=root, text='Latex Matrix generator')
label.pack(padx=0.5, pady=1)


# adding textbox
textbox = customtkinter.CTkTextbox(root)
textbox.pack(padx=0.5, pady=10)


# adding input field
entry = customtkinter.CTkEntry(master=root,
                               placeholder_text="Enter matrix",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.pack(padx=0.5, pady=0.5)




# adding confirmation button
def button_event():
    print("button pressed")
    state = entry.get()
    latex_code1 = generate_matrix(state)
    textbox.delete('0.0', 'end') # deleting contents
    textbox.insert('0.0', latex_code1) # inserting new content


        

button = customtkinter.CTkButton(master=root, text="Confirm", width=60, height=25, command=button_event)
button.pack(padx=20, pady=10)






root.mainloop()