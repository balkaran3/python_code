name=input('plz enter your name:')
print('helo',name)

message='''
How may i help you sir .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL'''
print(message)

task=int(input('plz insert your option:'))
available_amount= 5000
if task >= 1 and task<=3:
    print('welcome to you in virtual bank')
    if task==1:
        
        print('your available balance is:',available_amount)
        
        
    elif task == 2:
        deposit_amount=int(input('plz enter deposit amount'))
        if deposit_amount>=5000:
            available_amount=available_amount+deposit_amount
           
            print('you have successfully deposited amount',deposit_amount)
        else:
            ('plz enter amount more then 5000') 
        
    else:
        withdrawl_amount=int(input('plz enter your amount:'))
        if withdrawl_amount <= available_amount:
             available_amount -= withdrawl_amount
             print('you have successfully withdraw your amount:','your balance is',available_amount)
        else:
            print('you have not sufficient balance:')    
else:
    print('plz enter correct input')    