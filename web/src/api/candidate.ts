import type { Candidate, CandidatePaginatedResponse } from "../types/candidate";
import { api } from "./axios";

export const getCandidates = async (): Promise<CandidatePaginatedResponse> => {
    const { data } = await api.get("/candidates");

    return data;
};

export const getCandidate = async (
    id: string
): Promise<Candidate> => {
    const { data } = await api.get(`/candidates/${id}`);

    return data;
};

export const deleteCandidate = async (id: string) => {
    await api.delete(`/candidates/${id}`);
};