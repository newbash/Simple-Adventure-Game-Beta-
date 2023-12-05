answer = input("Would you like to play? (y/n)")

if answer.lower().strip() == "y":
    answer = input(
        "Looks like you ended up in a crossroad after trying to defeat the puppet master! would you like to go (right) or (left) to start your journey?").lower().strip()

    if answer == "right":
        answer = input("You encountered a gang member, would you like to (attack) or (flee)?").lower().strip()

        if answer == "attack":
            print("You killed the gang member and the rest of the gang are chasing you.")
        elif answer == "flee":
            print("You coward, You died of emotional damage.")
        else:
            print("Invalid choice, you lost.")

    elif answer == "left":
        answer = input("You fell into a lake and encountered a big fish, would you like to try to (catch) it or (swim) away?").lower().strip()
        if answer == "catch":
            print("You idiot, trying to catch a fish double your size with just bare hands. You're dead.")
        elif answer == "swim":
            print("You swam away from the fish and successfully escaped, choose an item and come back if you want.")

            answer = input("Choose an item (fishing rod) or (rifle)?")

            if answer == "fishing rod":
                answer = input("Would you like to go (back) and try to catch the big fish or would you like to (continue) your journey?").lower().strip()

            if answer == "back":
                answer = input("You caught the big fish successfully! would you like to go (sell) it in the Mountain Creek shop or would you like to (eat) it?")
            if answer == "sell":
                answer = input("You sold it for 25 gold.")
            elif answer == "eat":
                print("Oops it was poisonous, You Died.")


            elif answer == "rifle":
                answer = input("You picked rifle would you like to (train) in Mountain Creek to be an assassin or (hunt) in the nearby Firefly Forest?")

            if answer == "train":
                answer = input("Hello I'm Trainer Malik. I hear you want to be an assassin,well your at the right place! when do you want to start?(now/later)")

        else:
            print("Invalid choice, you lost.")

    else:
        print("Invalid choice, You lost.")

else:
    print("You're Not Okay.")
