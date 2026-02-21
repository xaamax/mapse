import { useQuery } from "@tanstack/react-query";
import { getPublicosAlvos, PublicoAlvoDTO } from "../services/publico-alvo-service";

export function useGetAllPublicosAlvos() {
  return useQuery({
    queryKey: ["publico-alvo"],
    queryFn: () => getPublicosAlvos(),
    select: (data) =>
      data.data?.map((s: PublicoAlvoDTO) => ({
        value: s.id,
        label: s.nome,
      })),
  });
}