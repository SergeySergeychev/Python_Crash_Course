
rounded_num  = int(round(10000.10, -1))
print(rounded_num)
score_test = "{:,}".format(rounded_num)
print(score_test)
"""
def rgb(r, g, b):
    # An empty list for rgb decimal numbers.
    rgb_dec = []
    # Append variables to the list.
    rgb_dec.append(r)
    rgb_dec.append(g)
    rgb_dec.append(b)
    # An empty string to contain r, g, b in hexadecimal representation.
    rgb_hex = ""
    # Loop to iterate values from 0 to 255.
    for color_num in rgb_dec:
        if int(color_num) < 0:
            rgb_hex += '00'
        elif 0 <= int(color_num) <= 15:
            hex_num = hex(color_num).replace('x','')
            rgb_hex += str(hex_num).upper()
        elif 15 < int(color_num) <= 255:
            hex_num = hex(color_num).lstrip('0x')
            rgb_hex += str(hex_num).upper()
        else:
            rgb_hex += 'FF'
    return rgb_hex

"""

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))
# r = -255
# g = 255
# b = 255
# print(rgb(r, g, b))
