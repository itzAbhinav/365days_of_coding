bits = int(input("Input a number of bits: "))

MB = bits // (1024*1024*8)
bits = bits % (1024*1024*8)

KB = bits // (1024*8)
bits = bits % (1024*8)

B = bits // 8
bits = bits % 8

print(f" {(MB*1024*1024*8) + (KB*1024*8) + (B*8) + bits} b = {MB} MB {KB} KB {B} B {bits} b")