import tkinter as tk
from tkinter import ttk
import seaborn as sns

class PaletteSelectorFrame(ttk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        
        self.callback = callback
        
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
        self.dropdown.pack(pady=10)
        
        # Button to show the selected palette
        self.show_button = ttk.Button(self, text="Show Palette", command=self.show_palette)
        self.show_button.pack(pady=10)
        
        # Canvas to display the palette colors
        self.canvas = tk.Canvas(self, width=300, height=50)
        self.canvas.pack(pady=10)
        
        # Button to confirm the selection
        self.confirm_button = ttk.Button(self, text="Confirm Selection", command=self.confirm_selection)
        self.confirm_button.pack(pady=10)
    
    def show_palette(self):
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
    
    def confirm_selection(self):
        # Call the callback function with the selected palette name
        self.callback(self.selected_palette.get())

# Example usage
def on_palette_selected(palette_name):
    print("Selected palette:", palette_name)

root = tk.Tk()
root.title("Palette Selector Example")

palette_selector = PaletteSelectorFrame(root, on_palette_selected)
palette_selector.pack(pady=20, padx=20)

root.mainloop()

