# Dictionaries Data Structure
new_D = {"Ronaldo": 36, "Messi": 34, "Salah": 27}
new_D1 = dict({'Dany': 33, 'Sane': 24, 'Sam': 30})
print(type(new_D))
print(type(new_D1))

# Sequence of tuples
children = dict({
    ("Child1", "5"),
    ("Child2", "6"),
    ("Child3", "7"),
})
print(type(children))

# Dictionary operations
print(new_D["Messi"])
new_D["Messi"] = 35
print(new_D)
del new_D["Messi"]
print(new_D)
print("Messi" in new_D)
