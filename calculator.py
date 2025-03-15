def simple_calculator(n,p, operation):
#asking the user for a number and operation.
 n=float(input("Enter the first number"))
 p=float(input("enter the second number"))
 operation=input("specify agin operation as +,*,-, or/")
 if operation=="+":
  result=n+p
 elif operation=="-":
  result=n-p
 elif operation=="*": 
  result=n*p
 elif operation=="/":
  if p==0:
   print("Error:divion by zero is impossible")
   return
  result=n/p
 else:
  print("Error! select a valid operation")
  return
 print(f"{n} {operation} {p} = {result}")
 #putting the calculatorn action by calling the function.
simple_calculator() 
 
 
