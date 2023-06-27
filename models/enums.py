import enum


class RoleType(enum.Enum):
    approver = "approver"
    complainer = "complainer"
    admin = "admin"


class ComplaintState(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
