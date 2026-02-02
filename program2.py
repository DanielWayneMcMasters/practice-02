# Nicholas Seward
# Temperature Converter
# AI Disclaimer: This code was written without the use of AI tools.

# Enter temperature in Celsius: 24
# 24.0°C = 75.2°F = 297.15K 

temp_C = float(input("Enter temperature in Celsius: "))

temp_F = (temp_C * 9/5) + 32
temp_K = temp_C + 273.15

print(f"{temp_C:.1f}°C = {temp_F:.1f}°F = {temp_K:.1f}K")

