
export interface Resume {
    id: string;
    candidate_id: string;
    file_name: string;
    pdf_path: string;
    resume_json: ResumeJson;
    created_at: string;
}


export interface ResumeJson {
    nome: string;
    email: string;
    telefone: string;
    endereco: string;
    linkedin: string;
    github: string;
    objetivo: string;
    resumo: string;

    formacao: Record<string, unknown>[];
    experiencia: Record<string, unknown>[];
    projetos: Record<string, unknown>[];

    tecnologias: string[];
    habilidades: string[];
    competencias: string[];
    cursos: string[];
    certificacoes: string[];
    idiomas: string[];
    premios: string[];
    publicacoes: string[];
    voluntariado: string[];

    informacoes_adicionais: string;

    [key: string]: unknown;
}