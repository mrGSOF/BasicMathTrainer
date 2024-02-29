import random
import winsound

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
        if Max <100:
           if a<b:
               a,b = Swap(a,b)
        c = a-b

    elif op=='/':
        c = a*b
        a,c = Swap(a,c)

    d = input("%d %s %d = "%(a,op,b))
    d = int(d)

    if c == d:
        return True
    return False

def Dice(Min=1, Max=7):
    x = int(random.uniform(Min,Max))
    return x

def DoubleDice(Min=1, Max=7):
    x1 = Dice(Min, Max)
    x2 = Dice(Min, Max)
    #print('%d, %d'%(x1,x2))
    return (x1, x2)


again = True
while again==True:
    again = False
    level = input('What level {A,B,C}?')
    level = level.lower()
    MaxNumber = 10
    if level=='a':
        print('Easy (0 to 10)')
        MaxNumber = 10

    elif level=='b':
        print('Medium (0 to 20)')
        MaxNumber = 20
                         
    elif level=='c':
        print('Hard (0 to 100)')
        MaxNumber = 100
    else:
        again = True

again = True
while again==True:
    op = input('What type {+,-,*,/}?')
    if ( (op=='+') or (op=='-') or (op=='*') or (op=='/') ):
        again = False

again = True
while again == True:
    counter = input('How many? ')
    if counter.isdigit():
        counter = int(counter)
        again = False

ErrCounter = 0
again = True
while again==True:
    Correct = Generate_Ex(op, MaxNumber)
    if Correct == True:
        print('VERY NICE!!!')
        winsound.PlaySound(sound_path+'DixieHorn.wav', winsound.SND_FILENAME)
        counter = counter -1
        if counter<1:
            again=False
    else:
        ErrCounter = ErrCounter +1
        print('Wrong #%d, Try another one.'%(ErrCounter))
        if (ErrCounter & 1)==1:
            winsound.PlaySound(sound_path+'HornHonk.wav', winsound.SND_FILENAME)
        else:
            winsound.PlaySound(sound_path+'DeepMaleBurp.wav', winsound.SND_FILENAME)
