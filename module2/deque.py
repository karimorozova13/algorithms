from collections import deque

# Двостороння черга,  "deque", "double-ended queue"

d = deque()
print(d)  

d.append('Mo')
d.appendleft('Kari')

d.popleft()

# Розширення extend
d.extend(['a', 'b', 'c'])
d.extendleft(['x', 'y', 'z'])
print(d)  

# Обертання rotation

# n - from end to start
d.rotate(2)
print(d)

# -n - from start to end

d.rotate(-2)
print(d)


# max_len
d1 = deque(maxlen=3)
d1.append('q')
d1.append('w')
d1.append('e')
print(d1)

d1.append('r')
print(d1)

# search
d2 = deque([1, 2, 3, 4, 2, 5])
print(d2.count(22))  # 2


