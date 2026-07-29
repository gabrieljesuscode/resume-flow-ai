export interface Candidate {
    id: string;
    name: string;
    email: string;
    phone: string;
    created_at: string;
}


export interface CandidateResponse {
    id: string;
    name: string;
    email: string;
    phone: string;
}


export interface CandidatePaginatedResponse {

    page: number;
    limit: string;
    count: number;
    total_candidates: number;
    candidates: CandidateResponse[]

}
