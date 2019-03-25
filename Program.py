import math
import random

#dapat dihapus, digunakan untuk melakukan visualisasi titik pencarian
import matplotlib.pyplot as plt

def rumus(x1, x2): 
    return -1*(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-(math.sqrt(math.pow(x1,2)+math.pow(x2, 2))/math.pi)))))

x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)
currentT = 1000
stopT = 1
coolRate = 0.999
currentState = rumus(x1,x2)
BSF = currentState
BSFA = x1
BSFB = x2

#arr dan arr2 dapat dihapus, digunakan untuk melakukan visualisasi titik pencarian
arr = []
arr2 = []

while(currentT>stopT):
    currentState = rumus(x1,x2)
    x1n = random.uniform(x1-(currentT/80),x1+(currentT/80))
    x2n = random.uniform(x2-(currentT/80),x2+(currentT/80))
    if(x1n<-10):
        x1n = -10
    elif(x1n>10):
        x1n = 10   
    if(x2n<-10):
        x2n = -10
    elif(x2n>10):
        x2n = 10
    nextState = rumus(x1n,x2n)
    selisihE = nextState - currentState
    if(selisihE<0):
        if(rumus(BSFA,BSFB)>rumus(x1n,x2n)):
            BSFA = x1n
            BSFB = x2n
            BSF = nextState
        x1 = x1n
        x2 = x2n
        currentState = nextState
    else:
        if(math.exp(-1*selisihE/currentT)<random.uniform(0,1)):
            x1 = x1n    
            x2 = x2n
            currentState = nextState

    #print di bawah digunakan untuk melihat perkembangan BSF dan suhu yang dilewati
    print(currentT,'\t',rumus(BSFA, BSFB))

    currentT = currentT*coolRate
    #dapat dihapus, digunakan untuk melakukan visualisasi titik pencarian
    arr.append(x1)
    arr2.append(x2)
    plt.plot(arr,arr2)
print("x1 : ",BSFA,'\t','x2 : ',BSFB)
print("Minimum Value: ",rumus(BSFA, BSFB))

#dapat dihapus, digunakan untuk visualisasi titik pencarian
plt.show()