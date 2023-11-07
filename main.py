p = float(input("Enter the principal interest rate : "))
r = float(input("Enter the rate: "))
time = int(input("Enter the time in years: "))
n = float(input("Enter the number of times interest rate is applied per time period: "))

##Simple Interest
si = p * (1 + (r * time))
ci = p * (1 + (r/n))**(n * time)

##Compound Interest
print(f'The simple interest is {si}')
print(f'The compound interest is {ci}')