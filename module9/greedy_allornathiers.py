# O(nlogn)

class Item:
    def __init__(self, weight, val) -> None:
        self.weight = weight
        self.val = val
        self.ratio = val / weight
        
def knapSack(items: list[Item], capacity: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_val = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_val += item.val
    return total_val

val1= Item(10, 60)
val2= Item(20, 100)
val3= Item(30, 120)
items = []

items.append(val3)
items.append(val1)
items.append(val2)


capacity = 50
print(knapSack(items, capacity)) 