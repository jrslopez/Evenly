class Group:
    def __init__(self, group_name, total_amount, balances=None):
        self.group_name = group_name
        self.total_amount = float(total_amount)
        self.balances = balances if balances else {}

    def to_dict(self):
        return {
            "group_name": self.group_name,
            "total_amount": self.total_amount,
            "balances": self.balances
        }
    
    def add_member(self, member_name):
        self.balances[member_name] = 0.0

    def split_evenly(self):
        num_members = len(self.balances)
        if num_members == 0:
            return
        
        split_amount = self.total_amount / num_members

        for member in self.balances:
            self.balances[member] = split_amount

    def display_group(self):
        print(f"Group Name: {self.group_name}")
        print(f"\nTotal Amount: {self.total_amount}")
        print(f"\nBalances:")
        for member, balance in self.balances.items():
            print(f"{member}: {balance}")