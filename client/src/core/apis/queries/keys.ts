export const dreKeys = {
  all: ["dre"] as const,
  detail: (id: string) => [...dreKeys.all, id] as const,
  filters: ({ }) => [...dreKeys.all] as const,
};

export const projetoSocialKeys = {
  all: ["projeto-social"] as const,
  detail: (id: string) => [...projetoSocialKeys.all, id] as const,
  filters: (filters: Record<string, string | number>) => [...projetoSocialKeys.all, ...Object.values(filters)] as const,
};