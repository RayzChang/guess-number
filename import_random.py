import random
start = input('請輸入起始範圍數字: ')
end = input('請輸入結束範圍數字: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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