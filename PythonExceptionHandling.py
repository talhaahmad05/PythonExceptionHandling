n=10
res=0
try:
    print("try")
    res=n/0
except Exception:
    print("Exception Block")
    print("Cant be Divided by zero")
else:
    print("Else Block")
    print(res)
finally:
    print("finally")