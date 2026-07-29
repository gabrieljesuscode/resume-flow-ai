import { api } from "./axios";
import type { Resume } from "../types/resume";

export async function getResumes(): Promise<Resume[]> {
    const { data } = await api.get("/resumes");
    return data;
}

export async function getResume(id: string): Promise<Resume> {
    const { data } = await api.get(`/resumes/${id}`);
    return data;
}

export async function getCandidateResumes(
    candidateId: string
): Promise<Resume[]> {
    const { data } = await api.get(`/candidates/${candidateId}/resumes`);
    return data;
}

export async function deleteResume(id: string): Promise<void> {
    await api.delete(`/resumes/${id}`);
}