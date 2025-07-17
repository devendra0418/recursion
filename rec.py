#fibonacci
'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
num=int(input("enter the terms:"))
for i in range(num):
    print(fib(i),end=" ")    '''

'''def dsum(n):
    if n==0:
        return 0
    return n%10 + temp(n//10)
def temp(n):
    return dsum(n)
num=int(input("enter 4 digit number:"))
print("sum of digits:",dsum(num))'''

'''def one(n):
    if n==0:
        return True 
    else:
        return two(n-1)
def two(n):
    if n==0:
        return False
    else:
        return one(n-1)
num=int(input("enter the number:"))
if one(num):
    print(num,"is even")
else:
    print(num,"is odd")            '''
'''
def A(n):
    if n<=0:
        return
    print("vijay",n)
    B(n-1)
def B(n):
    if n<=0:
        return
    print("deva",n)
    A(n-1)
num=int(input("ente rthe number:"))
A(num)'''

def player_A(n):
    if n<=0:
        print("player A reached 0!! player A loses")
        return
    print(f"\n player A's turn.current number{n}")
    move=int(input("player A, subtract 1 0r 2:"))
    player_B(n_move)
def player_B(n):
    if n<=0:
        print("player B reached 0!! player B loses")
        return
    print(f"\n player B's turn.current number{n}")
    move=int(input("player B,subtract 1 or 2:"))
    while move not in [1,2]:
        move=int(input("player B,subtract 1 or 2:"))
    player_A(n-move)
start=int(input("entering starting number:"))
player_A(start)    