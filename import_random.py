import random

r = random.randint(1, 100)

while True:
    user = input('請輸入數字:')
    user = int(user)

    if user == r:
        print('猜對了！')
        break
    
    elif user > r:
        print('比', user, '小')

    elif user < r:
        print('比', user, '大')