import random

r = random.randint(1, 100)
count = 0

while True:
    count += 1
    user = input('請輸入數字:')
    user = int(user)

    if user == r:
        print('猜對了！共猜了', count, '次')
        break
    
    elif user > r:
        print('比', user, '小')

    elif user < r:
        print('比', user, '大')

    print('這是你猜的第', count, '次')