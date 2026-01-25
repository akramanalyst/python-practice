import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())

i = 0
def demo():
    global i
    i+= 1
    print(i) 
    print("Hello Akram Jamal")
    demo()
demo()