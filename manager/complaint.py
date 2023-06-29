from sqlalchemy import select, insert, delete

from database import database
from models.complaint import Complaints
from models.enums import RoleType, ComplaintState


class ComplaintManager:

    @staticmethod
    async def get_complaints(user):
        query = select(Complaints)
        if user.role == RoleType.complainer:
            query = query.where(Complaints.complainer_id == user.id)
        elif user.role == RoleType.approver:
            query = query.where(Complaints.status == ComplaintState.pending)
        return await database.fetch_all(query)

    @staticmethod
    async def create_complaint(complaint_data, user):
        complaint_data["complainer_id"] = user.id
        id_ = await database.execute(insert(Complaints).values(complaint_data))
        return await database.fetch_one(select(Complaints).where(Complaints.id == id_))

    @staticmethod
    async def delete_complaint(complaint_id):
        await database.execute(delete(Complaints).where(Complaints.id == complaint_id))
