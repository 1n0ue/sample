while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    else:
        for height in range(h):
            for width in range(w):
                #print(height,width)
                if height > 0 and width > 0 and height < h-1 and width < w-1:
                    print(".",end='')
                elif width == w-1:
                    print("#")
                else:
                    print("#",end="")
    print("")