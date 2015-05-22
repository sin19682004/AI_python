def foo(a,b):
    return a+b
def f2((a,b)):
    a[0]=a[0]+1
    return

for i in range(10,1,-1):
    print i

List = range(1,6)
Tuple = (1,1),(2,4),(5,6),(1,2),(3,8)
Dic = {1:2,3:4,4:1,5:2}

print List
print Tuple
print Dic

#time2 =  { it*2:it for it in List }
time2 =  { (max(List)-List[i]+1)*2:List[i] for i in range(0,len(List)) }

print time2
print sorted(time2.items())

a = 2
print [i if i%2==0 else "A" for i in range(0,5) ]
print [ x*y for (x,y) in Tuple ]

print Dic[max(Dic)]
print max([Dic[i]for i in Dic])

print { foo(foo(i,1),1):i for i in List}
print min(List+[0])

print 1 if not [] else 0

m=([1],[2])
f2(m)
print m



