num = 0
lists = ["lists2[num]", "lists2[num]", "num-2"]
lists2 = ["human", "computer"]
i = 0

while i < 5:
    i += 1
    if eval(lists[num]) == 0:
        num = eval(lists[num])
    else:
        print(eval(lists[num]))
        num += 1