"""
Author: Thomas Skeens
Date written: 7/25/2024
Assignment: Module 08 Final Project Submission
Short Desc: Tom's Pizzeria ordering system. Users select items they want, calculate total and then submit their order
    
"""

import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying dialogs
from PIL import Image, ImageTk  # Import PIL for handling images


class TomsPizzeria:
    def __init__(self, root):
        """
        Initialize the GUI components of the application.
        :param root: The main window object.
        """
        self.root = root
        self.root.title("Tom's Pizzeria Supreme Pizza Lunch Special")  # Set the window title

        # Load and display images for the GUI
        try:
            pizza_image_path = "pizza.jpg"
            sides_image_path = "sides.jpg"
            drink_image_path = "drink.jpg"

            # Load and display the pizza image
            pizza_image = Image.open(pizza_image_path)
            # resizing pizza image
            pizza_image = pizza_image.resize((75,75))
            pizza_photo_image = ImageTk.PhotoImage(pizza_image)
            # Adding Pizza Label
            self.label_pizza_title = tk.Label(root,text="Pizza")
            self.label_pizza_title.grid(row=1,column=0,padx=10,pady=5)
            self.label_pizza_image = tk.Label(root, image=pizza_photo_image)
            self.label_pizza_image.image = pizza_photo_image  # Keep a reference to avoid garbage collection
            self.label_pizza_image.grid(row=1, column=0, rowspan=4, padx=10, pady=5)

            # Load and display the sides image
            sides_image = Image.open(sides_image_path)
            sides_image = sides_image.resize((75, 75))
            sides_photo_image = ImageTk.PhotoImage(sides_image)
            self.label_sides_title = tk.Label(root, text="Sides")
            self.label_sides_title.grid(row=4, column=0, padx=10, pady=5)
            self.label_sides_image = tk.Label(root, image=sides_photo_image)
            self.label_sides_image.image = sides_photo_image
            self.label_sides_image.grid(row=4, column=0, rowspan=4, padx=10, pady=5)

            # Load and display the drink image
            drink_image = Image.open(drink_image_path)
            drink_photo_image = ImageTk.PhotoImage(drink_image)
            self.label_drink_image = tk.Label(root, image=drink_photo_image)
            self.label_drink_image.image = drink_photo_image
            self.label_drink_image.grid(row=7, column=2, rowspan=2, padx=10, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")  # Print error if images fail to load

        # Customer Information section
        self.label_name = tk.Label(root, text="Name:")  # Label for name entry
        self.label_name.grid(row=0, column=1, padx=10, pady=5)  # Position the label
        self.entry_name = tk.Entry(root)  # Entry field for name
        self.entry_name.grid(row=0, column=2, padx=10, pady=5)  # Position the entry field

        self.label_phone = tk.Label(root, text="Phone:")  # Label for phone entry
        self.label_phone.grid(row=1, column=1, padx=10, pady=5)  # Position the label
        self.entry_phone = tk.Entry(root)  # Entry field for phone
        self.entry_phone.grid(row=1, column=2, padx=10, pady=5)  # Position the entry field

        # Pizza Selection section
        self.label_size = tk.Label(root, text=" Pizza Size:")  # Label for pizza size selection
        self.label_size.grid(row=2, column=1, padx=10, pady=5)  # Position the label
        self.size_var = tk.StringVar(value="Medium")  # Variable to hold selected size
        self.size_menu = tk.OptionMenu(root, self.size_var, "Small 9.99", "Medium 11.99", "Large 14.99")  # Dropdown menu for sizes
        self.size_menu.grid(row=2, column=2, padx=10, pady=5)  # Position the dropdown menu

        # Sides and Drinks section
        self.label_sides_drinks = tk.Label(root, text="Sides and Drinks")  # Label for sides and drinks
        self.label_sides_drinks.grid(row=3, column=1, columnspan=2, padx=10, pady=5)  # Position the label

        self.var_garlic_bread = tk.BooleanVar()  # Variable for garlic bread checkbox
        self.check_garlic_bread = tk.Checkbutton(root, text="Garlic Bread ($3.00)",
                                                 variable=self.var_garlic_bread)  # Checkbox for garlic bread
        self.check_garlic_bread.grid(row=4, column=1, padx=10, pady=5)  # Position the checkbox

        self.var_wings = tk.BooleanVar()  # Variable for wings checkbox
        self.check_wings = tk.Checkbutton(root, text="Wings ($5.00)", variable=self.var_wings)  # Checkbox for wings
        self.check_wings.grid(row=4, column=2, padx=10, pady=5)  # Position the checkbox

        self.var_soda = tk.BooleanVar()  # Variable for soda checkbox
        self.check_soda = tk.Checkbutton(root, text="Soda ($1.50)", variable=self.var_soda)  # Checkbox for soda
        self.check_soda.grid(row=5, column=1, padx=10, pady=5)  # Position the checkbox

        self.var_water = tk.BooleanVar()  # Variable for water checkbox
        self.check_water = tk.Checkbutton(root, text="Water ($1.00)", variable=self.var_water)  # Checkbox for water
        self.check_water.grid(row=5, column=2, padx=10, pady=5)  # Position the checkbox

        # Order Summary section
        self.label_total = tk.Label(root, text="Total: ")  # Label for total cost
        self.label_total.grid(row=6, column=1, padx=10, pady=5)  # Position the label
        self.total_var = tk.StringVar(value="0.0")  # Variable to hold total cost
        self.entry_total = tk.Entry(root, textvariable=self.total_var,
                                    state='readonly')  # Read-only entry for total cost
        self.entry_total.grid(row=6, column=2, padx=10, pady=5)  # Position the entry

        # Buttons section
        self.button_calculate = tk.Button(root, text="Calculate Total",
                                          command=self.calculate_total)  # Button to calculate total
        self.button_calculate.grid(row=7, column=1, padx=10, pady=5)  # Position the button

        self.button_submit = tk.Button(root, text="Submit Order", command=self.submit_order)  # Button to submit order
        self.button_submit.grid(row=7, column=2, padx=10, pady=5)  # Position the button

        self.button_exit = tk.Button(root, text="Exit", command=root.quit)  # Button to exit the application
        self.button_exit.grid(row=8, column=1, columnspan=2, padx=10, pady=5)
        # Position the entry

        # Buttons section
        self.button_calculate = tk.Button(root, text="Calculate Total",
                                          command=self.calculate_total)  # Button to calculate total
        self.button_calculate.grid(row=7, column=1, padx=10, pady=5)  # Position the button

        self.button_submit = tk.Button(root, text="Submit Order", command=self.submit_order)  # Button to submit order
        self.button_submit.grid(row=7, column=2, padx=10, pady=5)  # Position the button

        self.button_exit = tk.Button(root, text="Exit", command=root.quit)  # Button to exit the application
        self.button_exit.grid(row=8, column=1, columnspan=2, padx=10, pady=5)  # Position the button

    def calculate_total(self):
        """
        Calculate the total cost of the order based on selected items.
        """
        total = 0.0  # Initialize total cost
        size_price = {"Small 9.99": 9.99, "Medium 11.99": 11.99, "Large 14.99": 14.99}  # Price for each pizza size
        total += size_price[self.size_var.get()]  # Add the price of the selected size to the total

        # Add costs for selected sides and drinks
        if self.var_garlic_bread.get():
            total += 3.00
        if self.var_wings.get():
            total += 5.00
        if self.var_soda.get():
            total += 1.50
        if self.var_water.get():
            total += 1.00

        self.total_var.set(f"{total:.2f}")  # Update the total cost display

    def submit_order(self):
        """
        Submit the order and display the summary.
        """
        name = self.entry_name.get().strip()  # Get and strip whitespace from the name
        phone = self.entry_phone.get().strip()  # Get and strip whitespace from the phone

        # Input validation: Check if name and phone are not empty
        if not name or not phone:
            messagebox.showerror("Input Error", "Please enter both name and phone number.")  # Show error message
            return

        total = self.total_var.get()  # Get the total cost
        order_summary = f"Name: {name}\nPhone: {phone}\nTotal: ${total}"  # Create order summary
        messagebox.showinfo("Order Submitted", order_summary)  # Show order summary
        self.reset_fields()  # Reset all input fields

    def reset_fields(self):
        """
        Reset all input fields to default values.
        """
        self.entry_name.delete(0, tk.END)  # Clear the name entry
        self.entry_phone.delete(0, tk.END)  # Clear the phone entry
        self.size_var.set("Medium")  # Reset pizza size to Medium
        self.var_garlic_bread.set(False)  # Uncheck garlic bread checkbox
        self.var_wings.set(False)  # Uncheck wings checkbox
        self.var_soda.set(False)  # Uncheck soda checkbox
        self.var_water.set(False)  # Uncheck water checkbox
        self.total_var.set("0.0")  # Reset total cost to 0.0


if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = TomsPizzeria(root)  # Instantiate the application
    root.mainloop()  # Start the Tkinter event loop






