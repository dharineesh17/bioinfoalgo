p=[0,3,0,3,0,3]


seq=[0,3,0,3,0,3,0,3,1,0]


m = len(p)
print("m =",m)


n = len(seq)
print("n =",n)


k = n-m+1
print("k =",k)


pat = (p[5]+k*(p[4]+k*(p[3]+k*(p[2]+k*(p[1]+k*(p[0]))))))
print("pa=",pat)


t0 = (seq[5]+k*(seq[4]+k*(seq[3]+k*(seq[2]+k*(seq[1]+k*(seq[0]))))))
print("t0=",t0)


t1 = (k  *  (  t0  -  (k**(m-1))*seq[0]  ) ) + seq[m+0]
t2 = (k  *  (  t1  -  (k**(m-1))*seq[1]  ) ) + seq[m+1]
t3 = (k  *  (  t2  -  (k**(m-1))*seq[2]  ) ) + seq[m+2]
t4 = (k  *  (  t3  -  (k**(m-1))*seq[3]  ) ) + seq[m+3]

print("t1=",t1)
print("t2=",t2)
print("t3=",t3)
print("t4=",t4)






