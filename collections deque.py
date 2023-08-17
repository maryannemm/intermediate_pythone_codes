import collections
from collections import deque

groups=deque()
groups.extend(['newjeans','lesserafim','itzy','g-idle','pixy', 'twice', 'Mamamoo'])

groupss=['seventeen','TXT','BTS','stray kids','Enhypen', '2-pm','Shinee']
groups.extend(groupss)
print(sorted(groups))
groups.append('Dreamcatcher')
groups.append('Everglow')
print(sorted(groups))



# Create a deque with a maximum length of 3
my_deque = deque(maxlen=3)

# Add elements
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
print(my_deque)  # Output: deque([1, 2, 3], maxlen=3)

# Add one more element
my_deque.append(4)
print(my_deque)  # Output: deque([2, 3, 4], maxlen=3)
