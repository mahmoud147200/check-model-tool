import requests
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def check_imei_or_sn(identifier):
    """
    Function to check IMEI or Serial Number using the new API.
    """
    api_url = f"https://alpha.imeicheck.com/api/modelBrandName?imei={identifier}&format=html"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        raw_result = response.text.strip()
        
        # Formatting the output
        result_lines = raw_result.replace("<br>", "\n").split("\n")
        formatted_result = "\n".join(line.strip() for line in result_lines if line)
        
        return formatted_result
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def display_result(result):
    """
    Display the result inside the application output box.
    """
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state="normal")  # Ensure text is always copyable

def on_check():
    """
    Get input and perform API check.
    """
    identifier = entry.get().strip()
    if not identifier:
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a Serial Number or IMEI.")
        output_text.config(state="disabled")
        return
    result = check_imei_or_sn(identifier)
    display_result(result)

def on_clear():
    """
    Clear the input and output fields.
    """
    entry.delete(0, tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Abo Hany Bot")
root.geometry("450x400")
root.configure(bg="#1E1E1E")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12), background="#1E1E1E", foreground="white")

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(pady=20)

tk.Label(frame, text="Enter Serial Number or IMEI:", bg="#1E1E1E", fg="white", font=("Arial", 12)).pack(pady=10)
entry = ttk.Entry(frame, width=40, font=("Arial", 12))
entry.pack(pady=5)

button_frame = tk.Frame(frame, bg="#1E1E1E")
button_frame.pack(pady=10)

check_button = ttk.Button(button_frame, text="Check", command=on_check, style="TButton")
check_button.pack(side=tk.LEFT, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=on_clear, style="TButton")
clear_button.pack(side=tk.LEFT, padx=5)

output_text = ScrolledText(frame, width=50, height=10, font=("Arial", 12), wrap="word", bg="#2C2C2C", fg="white")
output_text.pack(pady=10, fill="both", expand=True)
output_text.config(state="disabled")

root.mainloop()
