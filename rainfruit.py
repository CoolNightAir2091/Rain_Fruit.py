import time
i = 80
y = 0.3
#fruits = ['Apple', 'Strawberry', 'Mango', 'Pineapple', 'Blueberry', 'Banana', 'Guava', 'Cherry']
fruits = [
    "Apple", "Apricot", "Avocado", "Açaí",
    "Banana", "Blackberry", "Blueberry", "Boysenberry",
    "Cantaloupe", "Cherimoya", "Cherry", "Clementine", "Coconut", "Cranberry",
    "Date", "Dragon Fruit", "Durian",
    "Fig", "Feijoa",
    "Grape", "Grapefruit", "Guava",
    "Honeydew", "Honeyberry",
    "Jackfruit", "Jujube",
    "Kiwi", "Kumquat",
    "Lemon", "Lime", "Lychee",
    "Mango", "Mangosteen", "Melon", "Honeydew", "Watermelon", "Cantaloupe",
    "Nectarine",
    "Orange",
    "Papaya", "Passion Fruit", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate",
    "Raspberry", "Rambutan",
    "Satsuma", "Strawberry",
    "Tamarind", "Tangerine",
    "Watermelon"
]

while fruits:
    #for fruit in fruits[:4]:
    for fruit in fruits:
        print(f"\n{fruit.center(i)}")
        time.sleep(y)
        i += 10
        if i == 350:
            i = 80
            y -= 0.05
        elif y < 0.06:
            y = 0.15
