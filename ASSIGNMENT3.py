import random as rd
n=100000
i=0
p=0
k=0
#theoritical probability
theoprob=3/8
print('Theoritical probability is:',theoprob)

#caluclating simulated probabilty
while i<n:
  x=rd.randint(1,2)
  if x==1:
   p=p+1
  x=rd.randint(1,2)
  if x==1:
    p=p+1
  x=rd.randint(1,2)
  if x==1:
    p=p+1
  x=rd.randint(1,2)
  if x==1:
    p=p+1
  if p==2:
    k=k+1
  i=i+1
  p=0
    
simprob=k/(n)
print('Simulated probability is:',simprob)