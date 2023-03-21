import random

maxim = 100
number=random.randint (1, maxim)
prime = 0
div_list = []

def prime_check () :
    global prime
    nr = 0
    for i in range(2, (int)(number/2) + 1):
        if number%i == 0 :
            nr += 1
            div_list.append (i)
    if nr == 0 :
        prime = 1
    
def compare (user_inp) :
    if user_inp < number :
        print("The number is bigger! Try again!")
    else:
        print("The number is smaller! Try again!")
        
def multiple () :
    temp=random.randint(2, 4)
    print("A multiple of the chosen number: ", temp * number)
    
def div ():
    if prime == 1 :
        multiple()
    else:
        temp=random.randint (0, len(div_list)-1)
        print("Divizor: ", div_list[temp])
        
        
prime_check()

used_divs = 0
used_mult = 0
used_compare = 0
score = 100
print("~ Number Guessing Game ~\nDon't let your score get to 0!")

while True and score > 0 :
    while True:             #loop to get player input
        user_input = (int)(input("Enter a number between 1 and 100: "))
        if user_input <= maxim and user_input >= 1 :
            break
    if user_input == number :  #input check
        print("Correct!")
        print("Final score: ", score)
        break
    else : 
        score -= 10
        if score == 0:
            print("Game over!")
            break
        hint_given = 0
        while hint_given == 0:
            temp = random.randint(1,3)
            if temp == 1 and used_compare == 0:
                compare(user_input)
                used_compare = 1
                used_divs = 0
                used_mult = 0
                hint_given = 1
                print("Score: ", score)
            if temp == 2 and used_mult == 0:
                multiple()
                used_mult = 1
                used_div = 0
                used_compare = 0
                hint_given = 1
                print("Score: ", score)
            if temp == 3 and used_divs == 0:
                div()
                used_divs = 1
                used_mult = 0
                used_compare = 0
                hint_given = 1
                print("Score: ", score)

    
                
                
                