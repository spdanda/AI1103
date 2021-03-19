import random as rd
import matplotlib.pyplot as plt
import numpy as np


z = 800000
list_of_cards = []
for i in range(1,53):
    list_of_cards.append(i)
#1-13 corresponds to all spade cards with 1 being king
#14-26 corresponds to all club cards with 14 being king
#27-39 corresponds to all diamond cards with 27 being king
#40-52 corresponds to all heart cards with 40 being king king
no_king_count = one_king_count = two_king_count = 0
for i in range(z):
    card_one = rd.randint(1,52)                                #for choosing first card
    r = list(range(1,card_one)) + list(range(card_one + 1,53)) #creating a list of cards excluding the first picked card
    card_two = rd.choice(r)                                    #for choosing the second card
    if card_one % 13 == 1 and card_two % 13 == 1:
        two_king_count += 1
    elif card_one % 13 == 1 or card_two % 13 == 1:
        one_king_count += 1
    else:
        no_king_count += 1

prob_no_king = no_king_count / z
prob_one_king = one_king_count / z
prob_two_king = two_king_count / z


No_of_kings =[0,1,2]
simulated_results = [prob_no_king,prob_one_king,prob_two_king]
theoretical_results = [0.850678733,0.14479638,0.004524887]

x = np.arange(len(No_of_kings))
plt.bar(x + 0.00, theoretical_results, color = 'red', width = 0.30, label = 'Theoretical results')
plt.bar(x + 0.30, simulated_results, color = 'blue', width = 0.30, label = 'Simulated results')
plt.xlabel('x = No.of kings obtained')
plt.ylabel('Pr(X=x) = Probabilty of obtaining x kings')
plt.xticks(x  + 0.30/2,[0, 1, 2])
plt.legend()
plt.show()
