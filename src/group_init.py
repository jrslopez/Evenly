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

group.split_evenly()    
new_group = group.to_dict()

try:
    with open("groups.json", "r") as f:
        groups = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    groups = []

groups.append(new_group)

with open("groups.json", "w") as f:
    json.dump(groups, f, indent = 4)