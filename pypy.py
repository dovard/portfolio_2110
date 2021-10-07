#'''
#  A=input()
# D,C,B=input().split()
# b=int(A)*int(B)
# c=int(A)*int(C)
# d=int(A)*int(D)
# print(b)
# print(c)
# print(d)
# print(b+(c*10)+(d*100))

# A=input()
# B,C,D=map(int,input.split())
# b=A*B
# c=A*C
# d=A*D
# print(d)
# print(c)
# print(b)
# print(d+(10*c)+(100*b))
'''
A=int(input())
B=input()
b=list(B)
# print(b[2])
# print(type(b[2]))
x=int(b[2])
y=int(b[1])
z=int(b[0])

a=A*x
b=A*y
c=A*z

# a=int(A)*(b[2])
# b=int(A)*(int(b[1]))
# c=int(A)*(int(b[0]))

print(a)
print(b)
print(c)
print(a+b*10+c*100)
'''
'''
A,B = input().split(" ")
A=int(A)
B=int(B)
if A>B:
  print(">")
elif A<B:
  print("<")
else:
  print("==")

'''
A=int(input())
B=input()
b=list(B)

c=[]
for i in b[::-1]:
  c.append(*A)
  print(c[i])

print(sum.list(c))
