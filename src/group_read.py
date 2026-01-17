from group import Group
import json

def load_groups(filename="groups.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    return data


def select_group(groups):

    for i, group in enumerate(groups):
        print(f"Number: {i+1}, Group: {group['group_name']}")

    selected_group_number = int(input("Choose a group number: ").strip())
    group_index = selected_group_number - 1

    selected = groups[group_index]

    selected_group = Group(
        groups[group_index]["group_name"],
        groups[group_index]["total_amount"],
        groups[group_index]["balances"]
    )

    return selected_group
