def reverseAlphabet(n):
    alpha = ord("A")
    for row in range(1,n + 1):
        for col in range(1,row + 1):
            print(chr(alpha + (n - col)),end="")
        print()

reverseAlphabet(5)