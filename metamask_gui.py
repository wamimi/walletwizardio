import tkinter as tk
import subprocess

def run_script():
    subprocess.run(["python3", "metamask_address_copier.py"])

root = tk.Tk()
root.title("MetaMask Address Copier")

button = tk.Button(root, text="Run MetaMask Address Copier", command=run_script)
button.pack(pady=20)

root.mainloop()