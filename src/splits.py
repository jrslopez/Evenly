from group_read import load_groups, select_group
import json

groups = load_groups()
chosen_group = select_group(groups)


for name in chosen_group.balances:
    chosen_group.balances[name] = 69
    print(f"{name}: {chosen_group.balances[name]}")

chosen_group.display_group()

with open("groups.json", "w") as f:
    json.dump(groups, f, indent=4)