from itemUnitGenerator.generator import *

item = Generator()
mob = Generator()

while True:
    print('1: Generate item\n2: Generate mob\n0: Exit')
    try:
        choice = int(input())
        if choice == 1:
            item.gen_item()
            print(item)
        elif choice == 2:
            mob.gen_unit()
            print(mob)
        elif choice == 0:
            break
    except ValueError as e:
        print(e)
        print('ENTER CORRECT NUMBER DUMBO')
