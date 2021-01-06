#!/bin/python3

# timeStamp = 939
IDs = [7, 13, 0, 0, 59, 0, 31, 19]

# timeStamp = 1000391
# IDs = ['19', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '37', 'x', 'x', 'x', 'x', 'x', '383', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '23', 'x', 'x', 'x', 'x', '13', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '29', 'x', '457', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '41', 'x', 'x', 'x', 'x', 'x', 'x', '17']

# num = 1068781

def check(num):
    for idx in range(1, len(IDs)):
        if IDs[idx] != 0:
            # val = IDs[idx]
            # print(idx, val - num % val)
            
            if idx == 0:
                if (num % IDs[idx] != 0):
                    return False
            
            elif (IDs[idx] - num % IDs[idx] != idx):
                return False
    
    return True

for num in range(7, 10**8, 7):
    if check(num):
        print(num)
        break

# print(check(146965))








# for ID in IDs:
#     if not ID.isalpha():
#         val = int(ID)
#         waitTime = val - timeStamp % val
#         print(val, waitTime, val * waitTime)
