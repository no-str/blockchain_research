from tkinter import *
from tkinter import ttk, Toplevel

import subprocess

def start_node():
    print("Starting Node @ IP " + ip.get() + " on Port " + str(port.get())
                    + ".")


root = Tk()
root.title("Node Creator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ip = StringVar(root, value='127.0.0.1')
port = StringVar(root, value='5000')
box = StringVar(root, value='1234')
recip = StringVar(root, value='http://127.0.0.1:5000/transactions/new')


ttk.Label(mainframe, text="IP").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Port").grid(column=1, row=2, sticky=W)


ip_entry = ttk.Entry(mainframe, width=10, textvariable=ip)
ip_entry.grid(column=2, row=1, sticky=W)

port_entry = ttk.Entry(mainframe, width=5, textvariable=port)
port_entry.grid(column=2, row=2, sticky=W)


ttk.Button(mainframe, text="Start", command=start_node).grid(column=4, row=1,
                sticky=E)

ip_entry.focus()

root.mainloop()
