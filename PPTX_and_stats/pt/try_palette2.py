import tkinter as tk
from tkinter import ttk
import seaborn as sns

class PaletteSelectorFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
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
        self.dropdown.bind("<<ComboboxSelected>>", self.show_palette)
        
        # Canvas to display the palette colors
        self.canvas = tk.Canvas(self, width=300, height=50)
        self.canvas.pack(pady=10)
        
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

# Example usage
def main():
    root = tk.Tk()
    root.title("Palette Selector Example")

    palette_selector = PaletteSelectorFrame(root)
    palette_selector.pack(pady=20, padx=20)

    root.mainloop()

if __name__ == "__main__":
    main()

