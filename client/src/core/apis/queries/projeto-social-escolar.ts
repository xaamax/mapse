import { useQuery } from "@tanstack/react-query";
import {
  getProjetosSociaisEscolares,
  getProjetoSocialEscolarDetalhes,
} from "@/core/apis/services/projeto-social-escolar-service";
import { projetoSocialEscolarKeys } from "./keys";

export function useGetAllProjetosSociaisEscolares(
  filters: Record<string, string | number>,
  enabled: boolean = true,
) {
  return useQuery({
    queryKey: projetoSocialEscolarKeys.filters(filters),
    queryFn: () => getProjetosSociaisEscolares(filters),
    enabled,
  });
}

export function useGetProjetoSocialEscolarPorUe(codigo_ue: string) {
  return useQuery({
    queryKey: projetoSocialEscolarKeys.detail(codigo_ue),
    queryFn: () => getProjetoSocialEscolarDetalhes(codigo_ue),
    enabled: !!codigo_ue,
  });
}
