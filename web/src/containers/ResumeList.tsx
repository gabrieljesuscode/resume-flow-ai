import { useCandidates } from "../hooks/useCandidates";
import { CandidateCard } from "./CandidateCard";

interface ResumeListProps {
  openResumesModal: () => void
}


export function ResumeList( { openResumesModal }: ResumeListProps ) {
  const { data, isLoading, error } = useCandidates();

  if (isLoading) {
    return <h1>Carregando...</h1>;
  }

  if (error) {
    return <h1>Erro ao carregar candidatos.</h1>;
  }

  if (data) return (


        <div className="flex flex-col mt-3 gap-4">
            { data.candidates.length !== 0 ?
            data.candidates.map((candidate, index) => (
                <CandidateCard key={index} candidate={candidate} openResumesModal={openResumesModal}/>
            ))
            :
            <div className="text-slate-800 px-3 py-2 bg-slate-200 rounded-lg text-sm">
                Nenhum currículo chegou aqui ainda!
            </div>
            }
        </div>

  );
}