print('---Welcom to Babs Calculator---')
while True:
 print('''
 ~press 1 for addition
 ~press 2 for substraction
 ~press 3 for multiplication
 ~press 4 for division
 ~press 0 for quit''')
 choice=int(input('Choose your option: '))
 if choice==1:
   num1=input('Enter first number: ')
   num2=input('Enter second number: ')
   try:
    sum=int(num1)+int(num2)
    print(f'{num1}+{num2}={sum}')
   except ValueError as e:
    print('only numbers are allowed!')  
 elif choice==2:
   num1=input('Enter first number: ')
   num2=input('Enter second number: ')
   try:
    difference=int(num1)-int(num2)
    print(f'{num1}-{num2}={difference}')
   except ValueError as e:
    print('only numbers are allowed!')   
 elif choice==3:
   num1=input('Enter first number: ')
   num2=input('Enter second number: ')
   try:
    product=int(num1)*int(num2)
    print(f'{num1}*{num2}={product}')
   except ValueError as e:
    print('only numbers are allowed!')  
 elif choice==4:
   num1=int(input('Enter first number: '))
   num2=int(input('Enter second number: '))
   try:
     quotient=num1/num2
     print(f'{num1}/{num2}={quotient}')
   except ZeroDivisionError as e:
     print('Can\'t divide with zero')
   except ValueError as e:
     print('only numbers are allowed!')    
 elif choice==0:
   print('See u next time...')
   break