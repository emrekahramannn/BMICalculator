# Import Module
import tkinter 

# Set The Screen
screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.config(padx=30, pady=30)
screen.minsize(400,300) # constant screen size
screen.maxsize(400,300) # constant screen size

#FONT 
FONT = ("Times New Roman", 14, "bold")


# LABELS and INPUTS

# WEIGHT INFORMATION
weight_label = tkinter.Label(text="Enter Your Weight (kg)", font=FONT)
weight_label.config(padx=8, pady=10)
weight_input = tkinter.Entry(width=12)
weight_input.focus()
weight_label.pack()
weight_input.pack()


# HEIGHT INFORMATION
height_label = tkinter.Label(text="Enter Your Height (cm)", font=FONT)
height_label.config(padx=8, pady=10)
height_input = tkinter.Entry(width=12)
height_label.pack()
height_input.pack()


# SPACE BETWEEN ENTRY-BUTON 
space = tkinter.Label(height=1)
space.pack()

# BUTTON
# BUTTON FUNCTION
def calculate_bmi():
    """
    When user click on button this function gets inputs
    which user wrote on Entry widgets. Then calculates
    the body mass index.
    """
    weight = weight_input.get().strip()
    height = height_input.get().strip()

    # if inputs are not given (empty string or space)
    if weight == "" or height == "":
        result_info.config(text="Enter both weight and height!")
    else:
        try:
            # convert str to float and cm to m
            bmi = float(weight) / ((float(height) / 100) ** 2)
        except ValueError:
            result_info.config(text="Invalid input! Please enter valid inputs.")
        else:
            write_result(bmi)
        
# BUTTON DESIGN
calculate_btn = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_btn.config(padx=8, pady=8, bg="grey")
calculate_btn.pack()


# RETURN INFO
result_info = tkinter.Label()
result_info.config(padx=8, pady=18, font=("Times New Roman", 10, "bold"))
result_info.pack()

# If user gave correct data run this function
def write_result(bmi):
    """
    This function informs the user according to his/her BMI ratio calculated
    by calculate_bmi function.
    """
    if bmi < 18.5:
        result_info.config(text=f"According to your BMI ratio, you are \"Underweight\"")
    elif 18.5 <= bmi <= 24.9:
        result_info.config(text=f"According to your BMI ratio, you are \"Normal\"")
    elif 25.0 <= bmi <= 29.9:
        result_info.config(text=f"According to your BMI ratio, you are \"Overweight\"")
    elif 30.0 <= bmi <= 39.9:
        result_info.config(text="According to your BMI ratio, you are \"Obese\"")
    else:
        result_info.config(text="According to your BMI ratio, you are \"Extremely Obese\"")



screen.mainloop()