import { useQuery } from "@tanstack/react-query";
import { getCategorias, CategoriaDTO } from "../services/categoria-service";

export function useGetAllCategorias() {
  return useQuery({
    queryKey: ["categoria"],
    queryFn: () => getCategorias(),
    select: (data) =>
      data.data?.map((s: CategoriaDTO) => ({
        value: s.id,
        label: s.nome,
      })),
  });
}