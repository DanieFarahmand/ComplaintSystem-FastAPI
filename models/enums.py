import enum


class RoleType(enum.Enum):
    approver = "Approver"
    complainer = "Complainer"
    admin = "Admin"


class ComplaintState(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
