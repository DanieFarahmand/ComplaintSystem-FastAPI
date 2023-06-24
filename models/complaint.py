from sqlalchemy import Table, Column, Integer, String, Text, Float, DateTime, ForeignKey, func, Enum
from models.enums import ComplaintState


class Complaints(Table):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    photo_url = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    create_date = Column(DateTime, server_default=func.utcnow())
    status = Column(Enum(ComplaintState), nullable=False, server_dfault=ComplaintState.pending.name)
    complainer_id = Column(ForeignKey("users.id"), nullable=False)

    def __str__(self):
        return f"{self.title}"
