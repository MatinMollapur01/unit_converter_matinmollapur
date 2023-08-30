import tkinter as tk
from tkinter import ttk


# Conversion functions
def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def km_to_meters(km):
    return km * 1000


def meters_to_km(meters):
    return meters / 1000


# Main conversion function
def convert_units():
    value = float(entry_value.get())
    source_unit = combo_source_unit.get()
    target_unit = combo_target_unit.get()

    # Convert source to km
    if source_unit == "Kilometers":
        value_in_km = value
    elif source_unit == "Miles":
        value_in_km = miles_to_km(value)
    elif source_unit == "Meters":
        value_in_km = meters_to_km(value)

    # Convert km to target
    if target_unit == "Kilometers":
        converted_value = value_in_km
    elif target_unit == "Miles":
        converted_value = km_to_miles(value_in_km)
    elif target_unit == "Meters":
        converted_value = km_to_meters(value_in_km)

    # Update the result label
    label_result.config(text=str(converted_value))


# Set up the main window
root = tk.Tk()
root.title("Unit Converter")

# Create and place widgets
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky=(tk.W, tk.E))

label_intro = ttk.Label(frame_input, text="Enter value and select units to convert:")
label_intro.grid(row=0, column=0, columnspan=2)

entry_value = ttk.Entry(frame_input, width=10)
entry_value.grid(row=1, column=0)

combo_source_unit = ttk.Combobox(frame_input, values=["Kilometers", "Miles", "Meters"], width=10)
combo_source_unit.grid(row=1, column=1)
combo_source_unit.set("Kilometers")

label_to = ttk.Label(frame_input, text="to")
label_to.grid(row=1, column=2)

combo_target_unit = ttk.Combobox(frame_input, values=["Kilometers", "Miles", "Meters"], width=10)
combo_target_unit.grid(row=1, column=3)
combo_target_unit.set("Miles")

button_convert = ttk.Button(frame_input, text="Convert", command=convert_units)
button_convert.grid(row=2, column=0, columnspan=4, pady=10)

label_result = ttk.Label(root, text="", padding="10")
label_result.grid(row=1, column=0, sticky=(tk.W, tk.E))

root.mainloop()
