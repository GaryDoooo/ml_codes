import tkinter as tk

root = tk.Tk()
root.title("Multiple Selection with Scrollbar")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=20, height=10)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

items = ["Item " + str(i) for i in range(1, 101)]  # Create 100 items
for item in items:
    listbox.insert(tk.END, item)

def get_selected():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected items:", selected_items)

select_button = tk.Button(root, text="Get Selected", command=get_selected)
select_button.pack(pady=5)

root.mainloop()
