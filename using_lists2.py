states = ["Washington", "Oregon", "California"]

for state in states:
    print(state)

states2 = ["Texas", "Florida", "Idaho"]
print("Washington" in states)
print("Tenesse " not in states)

states3 = states + states2
print(states3)


print(states[3:])
