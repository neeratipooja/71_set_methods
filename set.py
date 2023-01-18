# print(dir(set))
a={1,3,2}
b=4,'hi',7.6
a.add(b)
print(a)
n={10,20,30}
n.clear()
print(n)#set()
a={1,3,5};b={5,4,8};c={8,8,4};d={5,4,9}
print(a.intersection(b))#{5}
print(a.intersection(d))#{5}
print(b.intersection(c))#{8,4}
a={1,'hi',8.2};b={2.3,4,'hello'}
print(a.union(b))#{1,'hello',2.3,4,8.2,'hi'}
a.update(b)
print(a)
b.update(a)
print(b)
a={5,75,96};b={5,25,58,58,52}
print(a.difference(b))#{96,75}
print(b.difference(a))#{28,58,52}
print(a-b)#{96,75 }
print(b.difference_update(a))#none
k={34,21,53,45}
k.discard(22)
print(k)#{21,34,53,45}
k.discard(45)
print(k)#{21,34,53}
k.pop()
print(k)#{34,53,45}
a={1,2,3,4}
b={5,6,7}
c={4,5,6}
print('are a and b disjoint?',a.isdisjoint(b))#true
print('are a and c disjoint?',a.isdisjoint(c))#false
print('are b and c disjoint?',a.isdisjoint(c))#false
a={1,2,3,4}
b={5,6,7,1,2,3,4}
c={4,5,6,1,2}
print(a.issubset(b))#true
print(b.issubset(a))#false
print(a.issubset(c))#false
print(c.issubset(b))#true
d={24,75,41,36}
d.remove(42)
# print(d)#keyerror:42
a={8,9,10,12,14}
d={10,14,15,1}
print(a.issuperset(d))#false
q={8,9,10,12,14}
b={8,9,10}
print(q.issuperset(b))#true
print(b.issuperset(q))#false
print(q.issubset(b))#false
print(b.issubset(q))#true
a={1,2,3};b={4,3,3,6};c={10,15,20}
print(a.intersection(c))#set()