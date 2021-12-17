
def hello(i):
    if i!=0:
        print(i)
        hello(i-1)
    else:
        return

hello((int(input())))