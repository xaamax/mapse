import { useQuery } from "@tanstack/react-query";
import { getCamposTipos } from "../services/campo-service";

export function useGetAllCamposTipos() {
  return useQuery({
    queryKey: ["campos-tipos"],
    queryFn: () => getCamposTipos(),
    select: (data) =>
      data.data?.map((s: { label: string; value: number }) => ({
        value: s.value,
        label: s.label,
      })),
  });
}