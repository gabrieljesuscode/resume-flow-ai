import type { Resume } from "../types/resume";
import { Card } from "./Card";

interface ResumesModalProps {
    resumes: Resume[];
    isOpen: boolean;
    setClose: () => void
}

export function ResumesModal( { resumes, isOpen, setClose }: ResumesModalProps ){
    if (!isOpen) return null;

    return (
        <div className="flex justify-center items-center fixed inset-0 bg-black/40" onClick={setClose}>
            <Card className="flex items-start flex-col w-150 h-100">
                <div className="w-full h-full" onClick={(e) => e.stopPropagation()}>
                    <h1 className="text-xl font-medium">
                        Lista de Currículos Gabriel
                    </h1>


                    <div className="flex gap-2">
                        { resumes.length !== 0 ?
                            resumes.map((resume, index) => (
                                <div key={index} className="h-20 bg-amber-800 w-full flex justify-between items-center p-3 rounded-lg">
                                    {resume.file_name}
                                </div>
                            ))
                            :
                            "Nenhum currículo encontrado"

                        }
                    </div>
                </div>
            </Card>
        </div>
    )
}