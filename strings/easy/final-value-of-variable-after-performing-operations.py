operation = ["X++","++X","--X","X--"]

options = {
    "X++": 1,
    "++X": 1,
    "X--": -1,
    "--X": -1
}

new_list = []

for element in operation:
    for key, item in options.items():
        if element == key:
            new_list.append(options[key])
    
print(sum(new_list))
        