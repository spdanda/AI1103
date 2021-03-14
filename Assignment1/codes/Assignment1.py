import random


def prob_Reshma_winning(z):
    count = 0
    for i in range(z):
        # A number is randomly generated between 0 & z
        value = random.random();
        if value <= 0.62:
            pass
        else:
            # If the randomly generated number is greater than 0.62 then the value of count is incremented by 1
            count += 1
    #The value of the count indicates no.of times Reshma wins
    # when z matches are played and the simulated Probability is returned
    return count/z;


# Simulated Probability
print("Probability that Reshma wins according to simulation: ",prob_Reshma_winning(10**6))

# Theoretical Probability
print("Probability that Reshma wins actually is ",1-0.62)

