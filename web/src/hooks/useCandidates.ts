import { useQuery } from "@tanstack/react-query";
import { getCandidates } from "../api/candidate";

export function useCandidates() {
    return useQuery({
        queryKey: ["candidates"],
        queryFn: getCandidates,
    });
}