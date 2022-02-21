from tkinter.constants import CENTER
import tkinter as tk
import YTOS
import STOY

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YTOS OR STOY")
    root.geometry("800x800")
    root.resizable(height = None, width = None)

    canvas = tk.Canvas(root, bg = "#263")
    canvas.pack(fill="both", expand="true")

    ytosButton = tk.Button(canvas, text = "TRANSFER YOUTUBE SONGS TO SPOTIFY", command = YTOS.openYtosGui) 
    ytosButton.place(x = 500, y = 525)

    stoyButton = tk.Button(canvas, text = "TRANSFER SPOTIFY SONGS TO YOUTUBE", command = STOY.openStoyGui) 
    stoyButton.place(x = 75, y = 525)
    root.mainloop()
