
'''this code simulates flipping of coin.'''
import random

class Coin(object):
    '''this is a simple fair coin, can be pseudorandomly flipped'''
    sides = ('heads', 'tails')
    last_result = None
    
    def flip(self):
        '''call coin.flip() to flip the coin and record it as the last result'''
        self.last_result = result = random.choice(self.sides)
        return result
    
    # let's create some auxilliary functions to manipulate the coins:
def create_coins(number):
    '''create a list of a number of coin objects'''
    return [Coin() for _ in range(number)]
        
def flip_coins(coins):
    '''side effect function, modifies object in place, returns None'''
    for coin in coins:
        coin.flip()

def count_heads(flipped_coins):
    return sum(coin.last_result == 'heads' for coin in flipped_coins)

def count_tails(flipped_coins):
    return sum(coin.last_result == 'tails' for coin in flipped_coins)

from pylab import plot
import matplotlib.pyplot as plt
heads = []
def main():
    coins = create_coins(1000)
    for i in range(100):
        flip_coins(coins)
        heads.append(count_heads(coins))
        print (count_heads(coins))

if __name__ == '__main__':
    main()

#plot the heads
plot(range(100),heads)

#plot the histogram
plt.figure()
plt.hist(heads, histtype='bar')

'''not quite normal distribution but approximate.'''

import numpy as np
#experimenting
normal=[]
def main():
    for i in range(100):
        s = np.random.normal()
        normal.append(s)
        print(s)
if __name__ == '__main__':
        main()
#experimenting

#generating 1000 normal random data-points with mean = 0, SD = 1; then plotting the histogram and the normal distribution curve together
mean = 0
sigma = 1
s = np.random.normal(mean, sigma, 1000)
count, bins, ignored = plt.hist(s, 100, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mean)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()

