import math

with open('11.txt', 'r') as f:
    file = f.read().splitlines()

class Monkey:
  def __init__(self, num, it, op, op_amount, test, next_true, next_false):
    self.num = num
    self.items = it
    self.operation = op
    self.operation_amount = op_amount
    self.test = test
    self.next_true = next_true
    self.next_false = next_false
    self.activity = 0

# create monkeys
monkeys = []
for idx, line in enumerate(file):
    if line.startswith('Monkey'):
        num = int(file[idx].split(' ')[1].replace(':', ''))
        items = str.replace(file[idx+1][18:], ' ', '').split(',')
        items = [int(x) for x in items]
        op = file[idx+2][23:24]
        op_amount = file[idx+2][25:]
        op_amount = int(op_amount) if op_amount != 'old' else 0
        test = int(file[idx+3][21:])
        next_true = int(file[idx+4][29:])
        next_false = int(file[idx+5][30:])
        
        monkeys.append(Monkey(num, items, op, op_amount, test, next_true, next_false))

# run game part 1
for games in range(1,21):
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):            
            monkey.activity += 1
            
            if monkey.operation_amount == 0:
                new_item = math.floor((item * item) / 3)
            elif monkey.operation == "*":
                new_item = math.floor((item * monkey.operation_amount) / 3)
            elif monkey.operation == "+":
                new_item = math.floor((item + monkey.operation_amount) / 3)
            
            if new_item % monkey.test == 0:
                monkeys[monkey.next_true].items.append(new_item)
            else:
                monkeys[monkey.next_false].items.append(new_item)
        monkey.items = []

            
monkey_business = [x.activity for x in monkeys]
monkey_business.sort()

print(monkey_business[-1] * monkey_business[-2])

# run game part 2
for games in range(1,10001):
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):            
            monkey.activity += 1
            
            if monkey.operation_amount == 0:
                new_item = math.floor(item * item)
            elif monkey.operation == "*":
                new_item = math.floor(item * monkey.operation_amount)
            elif monkey.operation == "+":
                new_item = math.floor(item + monkey.operation_amount)
            
            if new_item % monkey.test == 0:
                monkeys[monkey.next_true].items.append(new_item)
            else:
                monkeys[monkey.next_false].items.append(new_item)
        monkey.items = []

            
monkey_business = [x.activity for x in monkeys]
monkey_business.sort()

print(monkey_business[-1] * monkey_business[-2])

