# Nicholas Seward
# Simple Calculator
# AI Disclaimer: This code was written without the use of AI tools.

# Enter first number: 14
# Enter second number: 8
# ==========================================
# Calculation Results
# ==========================================
# 14.00 + 8.00 = 22.00
# 14.00 - 8.00 = 6.00
# 14.00 * 8.00 = 112.00
# 14.00 / 8.00 = 1.75
# ==========================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("""
==========================================
CALCULATION RESULTS
==========================================""")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print("==========================================")

