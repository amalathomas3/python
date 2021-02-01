class login(Exception):pass
try:
  a=input("Username: ")
  b=input("password: ")
  i="amala"
  j="@12345"
  if a==i and b==j:
    print("Login successful")
  else:
    raise login("Invalid password or username")
except login as e:
  print(e)
