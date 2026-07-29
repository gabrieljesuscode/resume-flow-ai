from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db

from app.repositories.resumes_repository import ResumesRepository
from app.repositories.candidates_repository import CandidatesRepository
from app.schemas.resume import ResumeCreate, ResumeResponse


router = APIRouter(prefix="/resumes")

resumes_repository = ResumesRepository()
candidates_repository = CandidatesRepository()

@router.get("", response_model=list[ResumeResponse])
def get_all_resumes(
        limit: int = 10, 
        page: int = 1, 
        db: Session = Depends(get_db)
    ):

    if page < 1: 
        page = 1

    offset = (page - 1) * limit

    return resumes_repository.get_all(
            db,
            skip=offset,
            limit=limit,
            search=None
        )


@router.post("", response_model=ResumeResponse)
def create_candidate(
        resume: ResumeCreate,
        db: Session = Depends(get_db)
    ):

    db_candidate = candidates_repository.get_by_Email(db, resume.email)

    if not db_candidate:
        db_candidate = candidates_repository.create(
            db, 
            resume.name,
            resume.email,
            resume.phone
        )

    return resumes_repository.create(db, resume, db_candidate.id)


@router.get("/{resume_id}")
def get_resume_by_id(resume_id: str, db: Session = Depends(get_db)):

    found = resumes_repository.get_by_id(db=db,resume_id=resume_id)

    if not found:
        raise HTTPException(
            404,
            detail=f"Currículo {resume_id} não encontrado."
        )

    return found



@router.delete("/{resume_id}", status_code=204)
def delete_resume(resume_id: str, db: Session = Depends(get_db)):

    deleted = resumes_repository.delete_by_id(resume_id, db)

    if not deleted:
        raise HTTPException(
            404,
            detail=f"Currículo {resume_id} não encontrado."
        )

    return None
