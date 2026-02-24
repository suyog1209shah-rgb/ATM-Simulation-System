import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("ATM Simulator System")
root.geometry("400x400")
root.configure(bg="lightblue")
balance = 10000
correct_pin = "1234"
def login():
    entered_pin = pin_entry.get()
    if entered_pin == correct_pin:
        messagebox.showinfo("Login Success", "Welcome to ATM")
        show_menu()
    else:
        messagebox.showerror("Error", "Incorrect PIN")
def show_menu():
    login_frame.pack_forget()
    menu_frame.pack()
def check_balance():
    messagebox.showinfo("Balance", f"Your current balance is Rs. {balance}")
def deposit():
    global balance
    amount = amount_entry.get()
    if amount.isdigit():
        balance += int(amount)
        messagebox.showinfo("Success", "Amount Deposited Successfully")
        amount_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Enter valid amount")
def withdraw():
    global balance
    amount = amount_entry.get()
    if amount.isdigit():
        amount = int(amount)
        if amount <= balance:
            balance -= amount
            messagebox.showinfo("Success", "Withdrawal Successful")
            amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Insufficient Balance")
    else:
        messagebox.showerror("Error", "Enter valid amount")
def exit_app():
    root.destroy()

login_frame = tk.Frame(root, bg="lightblue")
login_frame.pack(pady=50)
tk.Label(login_frame, text="Enter PIN", font=("Arial", 14), bg="lightblue").pack(pady=10)
pin_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
pin_entry.pack(pady=10)
tk.Button(login_frame, text="Login", command=login, width=15, bg="green", fg="white").pack(pady=10)