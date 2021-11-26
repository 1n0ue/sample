while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    else:
        for height in range(h):
            if height % 2 == 0:
                for width in range(w):
                    if width % 2 == 0:
                        print("#",end="")
                    else:
                        print(".",end="")
                    if width == w-1:
                        print("")
            else:
                for width in range(w):
                    if width % 2 == 0:
                        print(".",end="")
                    else:
                        print("#",end="")
                    if width == w-1:
                        print("")
    print("")