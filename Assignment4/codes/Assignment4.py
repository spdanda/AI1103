import random
n=1000000 #no of times the experiment is conducted
i=0
p=0 #no of cases favourable for picking a  blue ball
#theoritical probabilities
P1=15/60 #P1 is theoritical probability of picking a blue ball
P2=45/59 #P2 is theoritical probability of selecting a black given a blue ball is picked
P3=P1*P2 #P3 is the reqired probability
print('theoritical probability of picking a blue ball is:',P1)
print('theoritical probability of picking a black ball given a blue ball is picked:',P2)
print('theoritical probability that first ball is blue and second ball is black is:',P3)
#caluclating simulated probabilities
while i<n:
  x=random.randint(1,60)#Assume 15 numbers represent 15 balls
  if x<=15:#Assume first 15 numbers represent 15 blue balls
    p=p+1
  i=i+1
P_1=p/n
i=0
k=0 #no of cases favorable for second ball as black given first is blue
while i<n:
  x=random.randint(1,59)#since 1st ball(blue) is taken out remaining balls count is 59
  if x<=45:#in that 59 assume 45 black balls represent first 45 numbers
    k=k+1
  i=i+1
P_2=k/n
m=0#no of cases favorable for first ball as blue and second as black
i=0
while i<n:
  x=random.randint(1,60)
  if x<=15:
   x=random.randint(1,59)
   if x<=45:
     m=m+1
  i=i+1
P_3=m/n
print('simulated probability of picking a blue ball is:',P_1)
print('simulated probability of picking a black ball given a blue ball is picked: ',P_2)
print('simulated probability that first ball is blue and second ball is black is:',P_3)
