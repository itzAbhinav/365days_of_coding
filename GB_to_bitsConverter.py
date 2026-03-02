def convertBytes(GB):
    bits = GB*1024*1024*1024*8
    Gigabytes = bits // (1024*1024*1024*8)
    bits = bits % (1024*1024*1024*8)
    Megabytes = bits // (1024*1024*8)
    bits = bits % (1024*1024*8)
    Kilobytes = bits // (1024*8)
    bits = bits % (1024*8)
    bytes = bits // 8
    bits = bits % 8

    print(f"{GB} GB = {int(Gigabytes)} GB, {int(Megabytes)} MB, {int(Kilobytes)} KB, {int(bytes)} B")

# compute the result, using multiple variables
GB = float(input("Input a number of gigabytes: "))

# output the result on one line (see examples)

convertBytes(GB)