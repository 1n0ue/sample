while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    else:
        for height in range(h):
            for width in range(w):
                if width == w-1:
                    print("#")
                else:
                    print("#" , end='')
        print()
 