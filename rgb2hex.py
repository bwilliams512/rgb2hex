"""
This is a calculator that can convert RGB values to 
Hexadecimal(hex) values and vice-versa.
"""

# create the rgb to hex method
def rgb_hex():
  invalid_msg = "Invalid value entered. Try again."
  
  red = int(input("Enter red (R) value: "))
  if (red < 0 or red > 255):
    print(invalid_msg)
    return

  green = int(input("Enter green (G) value: "))
  if (green < 0 or green > 255):
    print(invalid_msg)
    return

  blue = int(input("Enter blue (B) value: "))
  if (blue < 0 or blue > 255):
    print(invalid_msg)
    return
  
  # now use bitwise operators to build rest of our method
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())

# create the hex to rgb method
def hex_rgb():
  hex_val = input("Enter the color (six hexadecimal digits): ")
  if len(hex_val) != 6:
    print("Invalid hexidecimal value. Try again.")
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  
  print("Red: %s Green: %s Blue: %s" % (red, green, blue))

# create method that will run program
def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    # all cases of user input
    if option == '1':
      print("RGB to Hex...")
      rgb_hex()
    elif option == '2':
      print("Hex to RGB...")
      hex_rgb()
    elif option == 'X' or option == 'x':
      break
    else:
      print("Error")

convert()
