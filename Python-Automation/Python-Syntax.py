friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"];
for friend in friends:
    print(friend);
for index in range(5):
    if index == 0:
        print("First iteration");
    else:
        print("Not first iteration");
for index in range(3, 10):
    print(index);
for index in range(len(friends)):
    print(friends[index]);

for i in range(5):
    if i == 0:
        print("First iteration", i);
    else:
        print("Not first iteration", i);

import math;
print(7+5 * 2);
print(math.sqrt(36));
print(math.ceil(3.7));
print(math.floor(3.7));
print(math.pi);
