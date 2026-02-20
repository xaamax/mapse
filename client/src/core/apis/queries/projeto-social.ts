import { useQuery } from "@tanstack/react-query";
import { getProjetosSociais, getProjetoSocialDetalhes } from "@/core/apis/services/projeto-social-service";
import { projetoSocialKeys } from "./keys";

export function useGetAllProjetosSociais(
  filters: Record<string, string | number>,
  enabled: boolean = true
) {
  return useQuery({
    queryKey: projetoSocialKeys.filters(filters),
    queryFn: () => getProjetosSociais(filters),
    enabled,
  });
}

export function useGetProjetoSocialPorId(id: number) {
  return useQuery({
    queryKey: projetoSocialKeys.detail(id),
    queryFn: () => getProjetoSocialDetalhes(id),
    enabled: !!id,
  });
}
