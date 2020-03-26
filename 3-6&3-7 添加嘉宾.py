guests = ['shenjiabing','zhangmeng','wangjie','wangchao']
print("Now, I have a much bigger table to have dinner.So I will invite 3 more peple.")
guests.insert(0,'heyouyou')
guests.insert(5,'linling')
guests.append('luoqianxia')
for guest in guests:
    print("Dear " + guest + ", please come and enjoy dinner.")
print("The table cannot deliver on time, so I can only invite two friends to have a dinner.")
while(guests.__len__() > 2):
    guest = guests.pop()
    print("Sorry, " + guest + "we cannot have dinner tonight ,maybe we can do next time.")
print("Hey " + guests[0] + " and " + guests[1] + ", please come dinner tonight.")
del guests[0]
del guests[1]
print(guests)