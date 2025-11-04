### Cute math exercise software to train kids and teach procedural programming.
### By: Guy Soffer (GSOF) 2019

import random

try:
    import winsound
    print("Using winsound module")
    def playFile(filename) -> None:
        winsound.PlaySound(filename, winsound.SND_FILENAME)
except:
    try:
        import playsound
        print("Using playsound module")
        def playFile(filename) -> None:
            playsound.playsound(filename)
    except:
        print("No sound support\nPlease <pip install playsound>\nand retry\n")
        def playFile(filename) -> None:
            return
        
sound_path = './Sounds/'
def Swap(a,b):
    return (b,a)

def Generate_Ex(op, Max):
    a, b = DoubleDice(Min=0, Max=Max)

    if op=='+':
        c = a+b

    elif op=='*':
        c = a*b

    elif op=='-':
       ### Avoid negative results
        if a<b:
            a,b = Swap(a,b)
        c = a-b

    elif op=='/':
        ### Avoid devide by zero
        if b == 0:
            b = 1
        c = a
        a *= b

    ### Print the exercise
    d = input("%d %s %d = "%(a,op,b))
    d = int(d)

    if c == d:
        return True #< Correct
    return False #< Incorrect

def Dice(Min=1, Max=6):
    x = int(random.randint(Min,Max))
    return x

def DoubleDice(Min=1, Max=6):
    x1 = Dice(Min, Max)
    x2 = Dice(Min, Max)
    return (x1, x2)

def exercise(op="+", MaxNumber=10) -> bool:
    Correct = Generate_Ex(op, MaxNumber)
    if Correct == True:
        print('VERY NICE!!!')
        sndList = (sound_path+'Horn.wav',
                   sound_path+'DixieHorn.wav',
                   )
        playFile(sndList[Dice(0,len(sndList)-1)])
        return True
    else:
        print('Wrong #%d, Try another one.'%(ErrCounter))
        sndList = (sound_path+'HornHonk.wav',
                   sound_path+'DeepMaleBurp.wav',
                   sound_path+'Spring.wav',
                   )
        playFile(sndList[Dice(0,len(sndList)-1)])
        return True

try:
    import pysole
    ps = True
except:
    ps = False
    print("****************************************************")
    print("* For better visuals use <pip install liveconsole> *")
    print("****************************************************")

if ps:
    ### For better visuals
    pysole.probe(runRemainingCode=True,
                 printStartupCode=False,
                 primaryPrompt='math>> ',
                 font='Consolas',
                 fontSize=20,
                 )

again = True
while again == True:
    again = False
    print('A - Easy (Numbers between 0 to 10)')
    print('B - Medium (Numbers between 0 to 20)')
    print('C - Hard (Numbers between 0 to 100)')
    level = input('What level {A,B,C}? ')
    level = level.lower()
    MaxNumber = 10
    if level=='a':
        MaxNumber = 10

    elif level=='b':
        MaxNumber = 20
                         
    elif level=='c':
        MaxNumber = 100
    else:
        again = True

again = True
while again==True:
    op = input('Type of math operation {+,-,*,/}? ')
    if ( (op=='+') or (op=='-') or (op=='*') or (op=='/') ):
        again = False

again = True
while again == True:
    counter = input('How many exercises? ')
    if counter.isdigit():
        counter = int(counter)
        again = False

ErrCounter = 0
again = True
while again==True:
    correct = exercise(op, MaxNumber)
    if correct == True:
        counter = counter -1
        if counter < 1:
            again=False
    else:
        ErrCounter = ErrCounter +1

print("Try and type one of the lines below:")
print("exercise(op='+', MaxNumber=10)")
print("exercise(op='-', MaxNumber=20)")
print("exercise(op='*', MaxNumber=5)")
print("exercise(op='/', MaxNumber=8)")
