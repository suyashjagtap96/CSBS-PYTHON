import tkinter as tk

def calculate_total():
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        total = price * quantity
        label_result.config(text=f"Total Bill: ₹{total:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Billing System")

# Price entry
tk.Label(root, text="Item Price (₹):").grid(row=0, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=0, column=1, padx=10, pady=5)

# Quantity entry
tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Total Bill: ₹0.00", font=("Arial", 12, "bold"))
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
