#! /bin/env python3.12
# The above shebang probably shouldn't be used directly, but I want python version clearly documented here
# TODO: Fix this up in favor of a setup that favors a venv

import tkinter as tk
window = tk.Tk()

hand_display = tk.Label(text="Current hand:")
hand_display.pack()

window.mainloop()
