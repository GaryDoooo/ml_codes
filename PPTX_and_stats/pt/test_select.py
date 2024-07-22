import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Multiple Selection Box")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=20, height=5)
listbox.pack(padx=10, pady=10)

items = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew"]
for item in items:
    listbox.insert(tk.END, item)


def get_selected():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected items:", selected_items)


select_button = ttk.Button(root, text="Get Selected", command=get_selected)
select_button.pack(pady=5)

root.mainloop()
