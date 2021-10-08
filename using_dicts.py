state_capitals = {"Washington": "Olympia",
                  "California": "Sacramento", "Oregon": "Salem"}
print(state_capitals["Washington"])
print(state_capitals["California"])
state_capitals["Washington"] = "Aberdeen"
print(state_capitals)
state_capitals["Texas"] = 'Austin'
print(state_capitals)
del state_capitals["California"]
print(state_capitals)

removed = state_capitals.pop("Oregon")
print(state_capitals)
print(removed)

for a in state_capitals:
    print(a)
