from group import Group
import json

with open("groups.json", 'r') as f:
    data = json.load(f)

loaded_group = Group(
    data["group_name"],
    data["total_amount"],
    data["balances"]
)

loaded_group.display_group()