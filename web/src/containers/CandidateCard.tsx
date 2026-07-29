import { FilePen } from "lucide-react";
import type { CandidateResponse } from "../types/candidate";
import { Card } from "./Card";
interface CandidateCardProps {
    candidate: CandidateResponse;
    openResumesModal: (candidateId: string) => void;
}

export function CandidateCard({ candidate, openResumesModal }: CandidateCardProps){

    

    return (
        <Card className="cursor-pointer" onClick={() => openResumesModal(candidate.id)}>
            <div className="flex items-center gap-3 text-slate-700">
                
                <FilePen size={36}/>
                
                <div>

                    <h2 className="text-lg font-medium">
                        {candidate.name}
                    </h2>
                    <p className="text-sm">{candidate.email}</p>
                    <p className="text-sm">{candidate.phone}</p>
                
                </div>

            </div>

            

{/*             
            <div>
                <Trash/>
            </div> */}
        </Card>
    )
}