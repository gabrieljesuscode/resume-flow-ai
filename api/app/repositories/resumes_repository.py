from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.schemas.candidate import CandidateUpdate
from app.schemas.resume import ResumeCreate
from typing import Optional

class ResumesRepository():

    def __init__(self):
        pass

    def get_all(self, db: Session, skip: int = 0, limit: int = 10, search: str = None):
        """Retorna candidatos paginados e permite busca parcial por nome.

        skip: pula os primeiros registros.
        limit: quantidade máxima de registros retornados.
        search: filtro parcial case-insensitive pelo campo name.
        """
        query = db.query(Resume)

        if search:
            query = query.filter(Resume.name.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()



    def create(self, db: Session, resume: ResumeCreate, candidate_id: str):

        db_resume = Resume(
            candidate=candidate_id,
            vaga=resume.vaga,
            email_text=resume.email_text,
            data=resume.data
        )

        db.add(db_resume)
        db.commit()
        db.refresh(db_resume)

        return db_resume



    def get_by_id(self, db: Session, resume_id: str) -> Optional[Resume]:
        """Busca um resumo pelo ID."""
        return db.query(Resume).filter(Resume.id == resume_id).first()




    def update_by_id(
        self, 
        db: Session, 
        candidate_id: str, 
        candidate_data: CandidateUpdate
    ) -> Optional[Resume]:

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


    

    def delete_by_id(self, resume_id: str , db: Session):

        resume = self.get_by_id(db, resume_id)

        if not resume:
            return False

        db.delete(resume)
        db.commit()

        return True

    def resumes_by_id(self, candidate_id: str, db: Session):
        return db.query(Resume).filter(Resume.candidate_id == candidate_id).all()