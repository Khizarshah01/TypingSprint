from time import *
import random as r

def com(test,user):
    right=0
    error=0
    for i in range(len(test)):
        try:
            if test[i] != user[i]:
                error = error + 1
            elif test[i] == user[i]:
                right=right+1   
        except:
            error = error + 1
    a=len(test)
    b=right
    acc=(b*100)/a        
    return(error,acc,right)
    
h=0    
while h!=1:                        
    opt =["the solar system consists of the sun moon and planets.","hard work is worthless for those that don't believe in themselves." , "If you don't like the hand that fate's dealt you with, fight for a new one." , "the moment people come to know love, they run the risk of carrying hate."]
    test = r.choice(opt)
    print(test)
    print()
    
    start=time()
    test1=input("Enter - ")
    end=time()
    
    minute=(end-start)/60
    e=com(test,test1)
    print()
    
    print(f">>>>>Speed - {round((e[2]/minute)/5)}WPM")
    print(">>>>>>Errors - ",e[0])
    print(f">>>>>Accuracy - {round(e[1])}%")
    print()
    #Asking for repeat the program or not
    m=0
    while m!=1:
        k=input("********Can you try once more \n********yes/no :")
        if k=='yes':
            h=0
            m=1
        elif k=='no':
            h=1
            m=1
        else:
            print('>>>>>>Not in option')        
    
