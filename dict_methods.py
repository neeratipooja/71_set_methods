# print(dir(dict))
a={'p':'pooja','k':1,1:8,2:(4,6),3:['p','k'],4:{5,2.3}}
a.pop(2)
print(a)#{'p:'pooja','k':1,1:8,3:['p','k'],4:{5,2.3}}
a.popitem()
print(a)#{'p':'pooja','k':1,1:8,3:['p','k'],4:{5,2.3}}
print(a.keys())#{'p','k',1,2,3,4}
print(a.values())#{'pooja',1,8,(4,6),['p','k'],{2.3,5}}
a.clear()
print(a)#{}
a={1,8,9,4,3,5}
print(dict.fromkeys(a,'pass'))#{1:'pass',3:"pass",4:'pass',5:'pass',8:'pass',9:'pass'}
a={'p':'pooja','k':1,1:8,2:(4,6),3:['p','k'],4:{5,2.3}}
a.update({3:2.5})
print(a)#{'p':'pooja','k',1,1:8,2:(4,6),3:2.5,4:{2.3,5}}
a.update({5:1})
print(a)#{'p':'pooja','k':1,1:8,2:(4,6),3:2.5.4:{2.3,5}5:1}
a={1:4,2:5,3:'p',}
a.setdefault(1,'k')
print(a)#{1:4,2:5,3:'p'}
a.setdefault('p','hi')
print(a)#{1:4,2:5,3:'p','p':'hi'}
print(a.get(1))#4
print(a.get(5))#none
print(a.items())#((1,4),(2,5),(3,'p'))
a[1]='p'
print(a)#{1:'p',2:5,3:'p'}



