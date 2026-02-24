import { useQuery } from "@tanstack/react-query";
import { getFormularios, getFormularioDetalhes, getFormulariosOpcoes } from "@/core/apis/services/formulario-service";
import { formularioKeys } from "./keys";
import { FormularioDTO } from "@/core/dto/formulario-dto";

export function useGetAllFormularios(
  filters: Record<string, string | number>,
  enabled: boolean = true
) {
  return useQuery({
    queryKey: formularioKeys.filters(filters),
    queryFn: () => getFormularios(filters),
    enabled,
  });
}

export function useGetFormularioDetalhes(id: number) {
  return useQuery({
    queryKey: formularioKeys.detail(id),
    queryFn: () => getFormularioDetalhes(id),
    enabled: !!id,
  });
}

export function useGetFormulariosOpcoes() {
  return useQuery({
    queryKey: formularioKeys.all,
    queryFn: () => getFormulariosOpcoes(),
    select: (data) =>
      data.data?.map((s: FormularioDTO) => ({
        value: s.id,
        label: s.nome,
      })),
  });
}
