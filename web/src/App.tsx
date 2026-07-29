import { useState } from "react"
import { getCandidateResumes, type Resume } from "./api/resume"
import { Header } from "./containers/Header"
import { ResumeList } from "./containers/ResumeList"
import { ResumesModal } from "./containers/ResumesModal"

export default function App () {
  const [ openModal, setOpenModal ] = useState(false)
  const [ candidateResumes, setCandidateResumes ] = useState<Resume[]>([])


  const handleOpenModal = (candidateId: string) =>{
    setOpenModal(true)
    handleFetchResumes(candidateId)
  }
  const handleCloseModal = () =>{
    setOpenModal(false)
  }

  const handleFetchResumes = async (candidateId: string) => {
        const resumes = await getCandidateResumes(candidateId)
        setCandidateResumes(resumes)
    }

  return (
    <div className="flex items-center flex-col min-h-screen bg-slate-100 px-4">
        <ResumesModal isOpen={openModal} resumes={candidateResumes} setClose={handleCloseModal}/>
        <Header/>
        <h2 className="text-2xl font-medium text-slate-800 mt-5">
            Lista de Currículos
        </h2>
        <ResumeList openResumesModal={handleOpenModal}/>
    </div>
  )
}