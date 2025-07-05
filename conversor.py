import tkinter as tk
from tkinter import ttk
# No se espera sangría aquí, este es el lugar correcto para importar módulos o definir variables globales.
# Tasas de cambio de ejemplo 
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "NIO": 36.5
}

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            label_result.config(text="Selecciona monedas válidas")
            return
        result = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
        label_result.config(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    except ValueError:
        label_result.config(text="Introduce una cantidad válida")

# Crear ventana
root = tk.Tk()
root.title("Convertidor de Monedas")

# Widgets
tk.Label(root, text="Cantidad:").grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

tk.Label(root, text="De:").grid(row=1, column=0)
combo_from = ttk.Combobox(root, values=list(exchange_rates.keys()))
combo_from.grid(row=1, column=1)
combo_from.set("USD")

tk.Label(root, text="A:").grid(row=2, column=0)
combo_to = ttk.Combobox(root, values=list(exchange_rates.keys()))
combo_to.grid(row=2, column=1)
combo_to.set("EUR")

tk.Button(root, text="Convertir", command=convert_currency).grid(row=3, column=0, columnspan=2, pady=10)
label_result = tk.Label(root, text="Resultado")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
