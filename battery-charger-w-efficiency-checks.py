#Use a while loop with nested if statements to simulate a battery charging proces that includes efficiency checks.

current_level = int(input("What is your battery level at? "))

if current_level <= 100:
    while current_level <= 100:
        if current_level == 25:
            print("You're 1/4 of the way to full battery!")
        elif current_level == 50:
            print("You're half way to a full battery!")
        elif current_level == 75:
            print("You're 3/4 of the way to a full battery!")
        elif current_level == 100:
            print("You now have a full battery!")
            break
        current_level += 1
        #print(current_level)







