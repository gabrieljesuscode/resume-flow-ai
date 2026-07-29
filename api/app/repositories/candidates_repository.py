from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.models.resume import Resume
from app.schemas.candidate import CandidateUpdate
from typing import Optional

class CandidatesRepository():

    def __init__(self):
        pass

    def get_all(self, db: Session, skip: int = 0, limit: int = 10, search: str = None):
        """Retorna candidatos paginados e permite busca parcial por nome.

        skip: pula os primeiros registros.
        limit: quantidade máxima de registros retornados.
        search: filtro parcial case-insensitive pelo campo name.
        """
        query = db.query(Candidate)

        total_candidates = query.count()

        if search:
            query = query.filter(Candidate.name.ilike(f"%{search}%"))

        candidates = query.offset(skip).limit(limit).all()

        
        
        return {
            "page": (skip / limit) + 1,
            "limit": limit,
            "count": len(candidates),
            "total_candidates": total_candidates,
            "candidates": candidates
        }


    def create(self, db: Session, name: str, email: str, phone: str):

        candidate = Candidate(
            name,
            email,
            phone
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate


    
    def get_by_Email(self, db: Session, candidate_email: str) -> Optional[Candidate]:
        """Busca um candidato pelo Email."""
        return db.query(Candidate).filter(Candidate.email == candidate_email).first()




    def get_by_id(self, db: Session, candidate_id: str) -> Optional[Candidate]:
        """Busca um candidato pelo ID."""
        return db.query(Candidate).filter(Candidate.id == candidate_id).first()




    def update_by_id(
        self, 
        db: Session, 
        candidate_id: str, 
        candidate_data: CandidateUpdate
    ) -> Optional[Candidate]:

        candidate = self.get_by_id(db, candidate_id)
        
        if not candidate:
            return None

        # Extrai apenas os campos que foram enviados na requisição (exclui None)
        update_data = candidate_data.model_dump(exclude_unset=True)

        # Atualiza os atributos no objeto do SQLAlchemy
        for key, value in update_data.items():
            setattr(candidate, key, value)

        # Salva e atualiza o estado
        db.commit()
        db.refresh(candidate)

        return candidate


    

    def delete_by_id(self, candidate_id: str , db: Session):

        candidate = self.get_by_id(db, candidate_id)

        if not candidate:
            return False

        db.delete(candidate)
        db.commit()

        return True

    def resumes_by_id(self, candidate_id: str, db: Session):
        
        return db.query(Resume).filter(Resume.candidate == candidate_id).all()