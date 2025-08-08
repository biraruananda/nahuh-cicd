import tkinter as tk

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Setup window
root = tk.Tk()
root.title("Kalkulator")
root.geometry("300x400")

# Input
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid")
entry.pack(fill=tk.BOTH, padx=5, pady=5)

# Tombol
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

row_val = 0
col_val = 0
for b in buttons:
    btn = tk.Button(frame, text=b, font=("Arial", 18), height=2, width=5,
                    command=lambda x=b: click(x))
    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Resize grid
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
