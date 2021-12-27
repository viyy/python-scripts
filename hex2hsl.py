import sys
import hex2rgb

def rgb2hsl(rgb : tuple):
    _r = rgb[0]/255
    _g = rgb[1]/255
    _b = rgb[2]/255
    c_max = max([_r, _g, _b])
    c_min = min([_r, _g, _b])
    mode = 'r' if c_max == _r else 'g' if c_max == _g else 'b'
    d = c_max - c_min
    hue = 0
    if d == 0:
        hue = 0
    else:
        if mode == 'r':
            hue = 60 * (((_g - _b)/d) % 6)
        elif mode == 'g':
            hue = 60 * (((_b - _r)/d) + 2)
        else:
            hue = 60 * (((_r - _g)/d) + 4)
    lig = (c_max+c_min)/2 
    sat = 0 if d==0 else (d/(1-abs(2*lig-1)))
    return (round(hue), round(sat*100) , round(lig * 100))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        hex = sys.argv[1]
    else:
        print("input hex:\n")
        hex = input()
    print(rgb2hsl(hex2rgb.hex2rgb(hex)))