try:
    num = int(input("Enter a number: "))
    result = 10 / num  # May cause division by zero error
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter a valid number!")

finally:
    print("Execution completed!")
