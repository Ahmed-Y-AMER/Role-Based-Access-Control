ACTIONS = ("Create", "View", "Update", "Delete")
role_permissions = {"Admin": set(), "Manager": set(), "Customer": set()}
user_roles = {}


def grant_permission(role, action):
    if role not in role_permissions or action not in ACTIONS:
        raise ValueError("Unknown role or Account action.")
    role_permissions[role].add(action)


def assign_role(user, role):
    if role not in role_permissions:
        raise ValueError("Unknown role.")
    user_roles.setdefault(user, set()).add(role)


def can_access(user, action):
    return any(
        action in role_permissions[role] for role in user_roles.get(user, ())
    )


if __name__ == "__main__":
    for action in ACTIONS:
        grant_permission("Admin", action)
    grant_permission("Manager", "View")
    grant_permission("Manager", "Update")
    grant_permission("Customer", "View")

    assign_role("Ahmed", "Admin")
    assign_role("Maya", "Manager")
    assign_role("Omar", "Customer")

    print("Account access checks")
    print(f"{'User':<8} {'Role':<12}" + "".join(f"{a:>9}" for a in ACTIONS))
    for user in ("Ahmed", "Maya", "Omar", "Guest"):
        roles = ", ".join(sorted(user_roles.get(user, ()))) or "Unassigned"
        results = ["ALLOW" if can_access(user, a) else "DENY" for a in ACTIONS]
        print(f"{user:<8} {roles:<12}" + "".join(f"{r:>9}" for r in results))
