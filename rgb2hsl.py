import sys
import hex2hsl

if __name__ == '__main__':
    if len(sys.argv) > 3:
        r = sys.argv[1]
        g = sys.argv[2]
        b = sys.argv[3]
    else:
        print("input red (1-255):")
        r = input()
        print("input green (1-255):")
        g = input()
        print("input blue (1-255):")
        b = input()
    print(hex2hsl.rgb2hsl((int(r),int(g),int(b))))