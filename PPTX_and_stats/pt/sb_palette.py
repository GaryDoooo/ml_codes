def add_sb_palette_setting(        
# List of Seaborn palettes
    self.palettes = [
        "deep", "muted", "pastel", "bright", "dark", "colorblind",
        "Blues", "BuGn", "BuPu", "GnBu", "Greens", "Greys", "Oranges", 
        "Purples", "Reds", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd",
        "BrBG", "PiYG", "PRGn", "PuOr", "RdBu", "RdGy", "RdYlBu", 
        "RdYlGn", "Spectral"
    ]
    
    # Dropdown menu to select a palette
    self.selected_palette = tk.StringVar(value=self.palettes[0])
    self.dropdown = ttk.Combobox(self, textvariable=self.selected_palette, values=self.palettes)
    self.dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
    self.dropdown.bind("<<ComboboxSelected>>", self.show_palette)
    
    # Canvas to display the palette colors
    self.canvas = tk.Canvas(self, width=300, height=50)
    self.canvas.grid(row=0, column=1, padx=10, pady=10)
    
    # Buttons for confirm and cancel
    button_frame = ttk.Frame(self)
    button_frame.grid(row=1, column=0, columnspan=2, pady=10)
    
    self.confirm_button = ttk.Button(button_frame, text="Confirm", command=self.confirm_selection)
    self.confirm_button.pack(side=tk.LEFT, padx=5)
    
    self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.cancel_selection)
    self.cancel_button.pack(side=tk.LEFT, padx=5)
    
    # Display initial palette
    self.show_palette()

def show_palette(self, event=None):
    # Clear the canvas
    self.canvas.delete("all")
    
    # Get the selected palette
    palette_name = self.selected_palette.get()
    colors = sns.color_palette(palette_name, n_colors=6)
    
    # Display the colors as rectangles on the canvas
    for i, color in enumerate(colors):
        x0 = i * 50
        x1 = x0 + 50
        self.canvas.create_rectangle(x0, 0, x1, 50, fill=self.rgb_to_hex(color), outline="")

def rgb_to_hex(self, rgb):
    # Convert RGB tuple to hex color
    return '#%02x%02x%02x' % tuple(int(c * 255) for c in rgb)
