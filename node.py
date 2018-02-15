from tkinter import *
from tkinter import ttk

import subprocess

def start_node():
    node_add = 'python3 blockchain.py -p ' + str(port.get())
    subprocess.Popen(node_add, shell=True)
    print("Starting Node @ IP " + ip.get() + " on Port " + str(port.get()) + ".")

def stop_node():
#    subprocess.Popen.terminate(self)
    print("Stopping Node")

root = Tk()
root.title("Node GUI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ip = StringVar(root, value='127.0.0.1')
port = IntVar(root, value=5000)

ip_entry = ttk.Entry(mainframe, width=10, textvariable=ip)
ip_entry.grid(column=2, row=1, sticky=W)

port_entry = ttk.Entry(mainframe, width=5, textvariable=port)
port_entry.grid(column=2, row=2, sticky=W)

ttk.Button(mainframe, text="Start", command=start_node).grid(column=4, row=1, sticky=E)
ttk.Button(mainframe, text="Stop", command=stop_node).grid(column=4, row=2, sticky=E)

ttk.Label(mainframe, text="IP").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Port").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

ip_entry.focus()
root.bind('<Return>')

root.mainloop()
