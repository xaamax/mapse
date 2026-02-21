import { useQuery } from "@tanstack/react-query";
import { getSituacoes, SituacaoDTO } from "../services/situacao-service";

export function useGetAllSituacoes() {
  return useQuery({
    queryKey: ["situacao"],
    queryFn: () => getSituacoes(),
    select: (data) =>
      data.data?.map((s: SituacaoDTO) => ({
        value: s.id,
        label: s.nome,
      })),
  });
}