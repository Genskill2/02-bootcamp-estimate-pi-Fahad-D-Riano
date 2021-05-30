halfpi=1.0
n=20
for i in range(1,n):
   numo=i*2
   denom=i*2-1
   halfpi=halfpi * (numo*numo) / (denom *(denom + 2))
print(2* halfpi)