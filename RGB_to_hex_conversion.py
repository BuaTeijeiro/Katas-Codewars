import string

def rgb(r, g, b):
    def approximate_RGB (number):
        if number <0:
            return 0
        elif number >255:
            return 255
        else:
            return round(number)
    def to_hexadecimal(number):
        hexadecimal=string.hexdigits[:16]
        return hexadecimal[number // 16] + hexadecimal[number % 16]
    r_corrected = approximate_RGB (r)
    g_corrected = approximate_RGB (g)
    b_corrected = approximate_RGB (b)
    
    code_RGB = to_hexadecimal(r_corrected) + to_hexadecimal(g_corrected) + to_hexadecimal(b_corrected)
    return code_RGB.upper()