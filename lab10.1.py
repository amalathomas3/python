try:
  a=int(input("enter numerator : "))
  b=int(input("enter denominator : "))
  print('%d/%d=%f'%(a,b,a/b))
except (ZeroDivisionError,ValueError) as e:
  print(e)
else:
  print("Division successful")
finally:
  print("Excecuted always")
