import sys

def hex2rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        hex = sys.argv[1]
    else:
        print("input hex:\n")
        hex = input()
    print(hex2rgb(hex))