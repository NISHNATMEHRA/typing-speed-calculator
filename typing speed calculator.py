#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
                error=error+1                   
    return error


def speed_time(time_s,time_e,userinput):
    time_delay = time_e-time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
    ck=input("Do you Ready: (yes / No) ")
    if ck=="Yes" or ck=="yes":
        test=['''Friendship is one of the greatest blessings that not everyone is lucky enough to have. We meet a 
        lot of people in the journey of life but there are only a few who leave a mark on us. My best friend is 
        one such person who has been able to make a positive impact on my life. We have been a part of each other’s
        lives for the longest time and our friendship is still developing. She has been with me through all the 
        thicks and thins. Most importantly, I feel extremely fortunate to have someone as a best friend in my life. 
        In this essay on my best friend, I will tell you about how we became friends and about her best qualities.''',
        '''The dog is a pet animal. A dog has sharp teeth so that it can eat flesh very easily, it has four legs, 
        two ears, two eyes, a tail, a mouth, and a nose. It is a very clever animal and is very useful in catching 
        thieves. It runs very fast, barks loudly and attacks the strangers. A dog saves the life of the master from 
        danger. One can find dogs everywhere in the world. Dogs are a very faithful animal. It has a sharp mind and
        a strong sense of hearing smelling the things. It also has many qualities like swimming in the water, 
        jumping from anywhere, good smelling sense.''',
        '''It is a well-known fact that a person without an aim is a person without a life. All the creatures in 
        this universe have one or another specific aim. It is common for all things. As the human is the best 
        creature among them all, he has been given a right to select what he wants to do in his life. The mindset 
        of each and every person is of its own type. Therefore, his aim in life will also be different from others''',
        '''Books are friends who never leave your side. I find this saying to be very true as books have always been 
        there for me. I enjoy reading books. They have the power to help us travel through worlds without moving from 
        our places. In addition, books also enhance our imagination. Growing up, my parents and teachers always 
        encouraged me to read. They taught me the importance of reading. Subsequently, I have read several books. 
        However, one boom that will always be my favourite is Harry Potter. It is one of the most intriguing reads 
        of my life. I have read all the books of this series, yet I read them again as I never get bored of it.''',
        '''Pollution is a term which even kids are aware of these days. It has become so common that almost everyone 
        acknowledges the fact that pollution is rising continuously. The term ‘pollution’ means the manifestation of 
        any unsolicited foreign substance in something. When we talk about pollution on earth, we refer to the 
        contamination that is happening of the natural resources by various pollutants. All this is mainly caused by 
        human activities which harm the environment in ways more than one. Therefore, an urgent need has arisen to 
        tackle this issue straightaway. That is to say, pollution is damaging our earth severely and we need to 
        realize its effects and prevent this damage. In this essay on pollution, we will see what are the effects of
        pollution and how to reduce it.''']
        test1=r.choice(test)

        print("*********Typing speed checker*********")
        print(test1)
        print("_"*100)
        print()
        time_1=time()
        testinput=input("Enter: ")
        time_2=time()

        print("speed: ",speed_time(time_1,time_2,testinput),"word/sec")
        print("error: ",mistake(test1,testinput))
    elif ck=="no" or ck=="No":
        print(" ****************thankyou*************** ")
        break
    else:
        print("Wrong input")
        

