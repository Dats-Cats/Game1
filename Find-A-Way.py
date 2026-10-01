#finding a way

import random

print('Select difficulty level')
difficulty=int(input())
finding=0
way=[]
step=0
while True:
    while finding < difficulty:
        print('right or left')
        going=str(input())
        step=step+1
        if going==('right'):
            finder=random.randint(1,2)
            finder2 = random.randint(1, 2)
            if finder==finder2:
                finding=finding+1
            else:
                print('you found nothing')
            way.append('right')
        if going==('left'):
            finder = random.randint(1, 2)
            finder2 = random.randint(1, 2)
            if finder==finder2:
                finding = finding + 1
            else:
                print('you found nothing')
            way.append('left')
        if step>=3:
            if way[step-1] == way[step-2] == way[step-3]:
                finding = finding-3
                print('ты в петле чувак')

        print('you found exit')
        print('your way was:',list)

