from typing import List

from fastapi import APIRouter, Request, Depends

from manager.complaint import ComplaintManager
from manager.auth import oauth2_scheme, is_complainer, is_admin, is_approver
from schemas.complaint import ComplaintIn, ComplaintOut

router = APIRouter(tags=["Complaint"])


@router.get("/get_complaints/", dependencies=[Depends(oauth2_scheme)], response_model=List[ComplaintOut])
async def get_complaints(request: Request):
    user = request.state.user
    complaints = await ComplaintManager.get_complaints(user)
    return complaints


@router.post("/complaints/", dependencies=[Depends(oauth2_scheme), Depends(is_complainer)],
             response_model=ComplaintOut)
async def create_complaints(request: Request, complaint: ComplaintIn):
    user = request.state.user
    return await ComplaintManager.create_complaint(complaint.dict(), user)


@router.delete("/complaints/{complaint_id}", dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
               status_code=204)
async def delete_complaint(complaint_id: int):
    await ComplaintManager.delete_complaint(complaint_id)
