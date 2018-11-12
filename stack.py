"""
1. Create a class Stack with instance variable items initialized to an empty list.
2. Define methods push, pop and is_empty inside the class Stack.
3. The method push appends data to items.
4. The method pop pops the first element in items.
5. The method is_empty returns True only if items is empty.
"""


class stack:
    items = []

    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f"stack items: {self.items}"

    def push(self,value):
        return self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


stk1 = stack([3, 4, 5, 6])
stk1.push(9)
print(stk1)
stk1.pop()
print(stk1)
print(stk1.is_empty())


stk2 = stack([6333,6314,6359,6308])
stk2.push(6315)
print(stk2)
stk2.pop()
print(stk2)
print(stk2.is_empty())