from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db

from app.repositories.candidates_repository import CandidatesRepository
from app.schemas.candidate import CandidateCreate, CandidateResponse, CandidateUpdate, CandidatePaginatedResponse


router = APIRouter(prefix="/candidates")

candidates_repository = CandidatesRepository()

@router.get("", response_model=CandidatePaginatedResponse)
def get_all_candidates(
        limit: int = 10, 
        page: int = 1, 
        db: Session = Depends(get_db)
    ):

    if page < 1: 
        page = 1

    if limit < 0:
        limit = 0

    offset = (page - 1) * limit

    return candidates_repository.get_all(
            db,
            skip=offset,
            limit=limit,
            search=None
        )


@router.post("", response_model=CandidateResponse)
def create_candidate(
        candidate: CandidateCreate,
        db: Session = Depends(get_db)
    ):

    return candidates_repository.create(
        db,
        candidate.name,
        candidate.email,
        candidate.phone
    )


@router.put("/{candidate_id}", response_model=CandidateResponse)
def update_candidate(
        candidate_id: str,
        candidate_data: CandidateUpdate,
        db: Session = Depends(get_db)
    ):

    updated_candidate = candidates_repository.update_by_id(
        candidate_data=candidate_data, 
        candidate_id=candidate_id, 
        db=db
        )

    if not updated_candidate:
        raise HTTPException(
            404,
            detail=f"Candidato {candidate_id} não encontrado."
        )

    return updated_candidate




@router.delete("/{candidate_id}", status_code=204)
def delete_candidate(candidate_id: str, db: Session = Depends(get_db)):

    deleted = candidates_repository.delete_by_id(candidate_id, db)

    if not deleted:
        raise HTTPException(
            404,
            detail=f"Candidato {candidate_id} não encontrado."
        )

    return None


@router.get("/{candidate_id}/resumes")
def get_all_candidate_resumes(candidate_id: str, db: Session = Depends(get_db)):
    return candidates_repository.resumes_by_id(
        candidate_id=candidate_id,
        db=db
    )