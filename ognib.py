"""Simulate Ognib, when does the first mumber get un-dabbed
"""

from numpy import *
import matplotlib.pyplot as plt
import logging

def new_board():
    cols = arange(1,76).reshape(5,15)
    return array([random.permutation(c)[:5] for c in cols])

def new_game():
    balls=random.permutation(arange(1,76))
    return balls

def main():
    nbins = 25   
    mycard=new_board()
    counter=0
    games=10**6
    games_sep = (format(games, ',d'))
    ognib=[]
    print("Your Card Sir:")
    print(mycard)
    print("Eyes Down for",games_sep,"games")
    # How many balls are called until first ball is undabbed
    while counter<games:
        theballs=new_game()
        called=0
        for ball in theballs:
            if ball in mycard:
                ognib.append(called)
                break
            called= called + 1
        counter=counter+1
    #print(ognib)
    nbins= max(ognib)
    x = range(0,nbins) 
    xi = list(range(len(x)))  
    plt.hist(ognib, nbins )
    title=games_sep+" games of Ognib"
    plt.title(title)
    plt.xlabel('Draws before full house')
    plt.ylabel('How many times')
    plt.xticks(xi, x)
    #plt.yscale("log")
    plt.show()
if __name__ == "__main__":
    main()
