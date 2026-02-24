num_dict = dict()  # dictionary for containin numbers
A = 0             # initial area = W*L
W = int(input())  # width W
N = int(input())  # number of cakes

## store integers from 1-10000
for i in range(1, 10000):
    num_dict[str(i)] = i

## calculate area A
for n in range(N):
    cake = input().split()
    #A += int(cake[0])*int(cake[1])
    A += num_dict[cake[0]]*num_dict[cake[1]]
print(A//W)       # length L
