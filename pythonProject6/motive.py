name = input('What is your name? ')
age = input("When were you born? ")
x = 2022-int(age)

if int(age) >= 2021:
    print(name.upper(), 'Invalid age Input, Restart the program to Re-enter your age. GoodLuck' .upper())
    print('error', exit())
print('Good morning ' + name, "you are " + str(x), 'years old')

if x > 18:
    print(name, 'you are an adult, Take care when playing with girls. '
                'Avoid becoming a father coz you are now a potential one. '
                'Work Hard in whatever You do '
                'It is always a great idea to keep Hoping for the best. '
                'Stay Strong and Have a Nice Day '+name.upper())

else:
    print(name, 'you are not yet to be an adult, '
                'Work hard in your studies for a better tomorrow. '
                'The future is always bright young '+name.upper(),
          'have the best of it')
