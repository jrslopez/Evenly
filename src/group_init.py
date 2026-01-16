import json
from group import Group

group_name_input = input("Enter Group Name: ")
total_amount_input = input("Enter total amount: ")

group = Group(group_name_input, total_amount_input)

print("\nEnter the names of members then type done when finished:")
while True:
    member = input("Member Name: ").strip()
    if member.lower() == 'done':
        break
    if member:
        group.add_member(member)

with open("groups.json", "a") as f:
    json.dump(group.to_dict(), f, indent = 4)