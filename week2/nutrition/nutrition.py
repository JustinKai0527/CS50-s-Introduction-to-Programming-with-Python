
fruit = input("Item: ").lower()

calories = {
    "apple": 130,
    "avocado": 50,
    "cantaloupe": 50,
    "grapes": 90,
    "kiwifruit": 90,
    "lime": 20,
    "orange": 80,
    "pear": 100,
    "plums": 70,
    "sweet cherries": 100,
    "watermelon": 80,
    "banana": 110,
    "grapefruit": 60,
    "honeydew melon": 50,
    "lemon": 15,
    "nectarine": 60,
    "peach": 60,
    "pineapple": 50,
    "strawberries": 50,
    "tangerine": 50
}

if fruit in calories:
    print(f"Calories: {calories[fruit]}")
