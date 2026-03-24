print("Hello World")
n=10
res=0
try:
    res=n/0
except ZeroDivisionError:
    print("Cant be Divided by zero")
print(res)