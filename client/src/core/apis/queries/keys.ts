import { closeAuth } from './../../hooks/use-auth-operations';
export const dreKeys = {
  all: ["dre"] as const,
  detail: (id: string) => [...dreKeys.all, id] as const,
  filters: ({ }) => [...dreKeys.all] as const,
};

export const projetoSocialKeys = {
  all: ["projeto-social"] as const,
  detail: (id: number) => [...projetoSocialKeys.all, id] as const,
  filters: (filters: Record<string, string | number>) => [...projetoSocialKeys.all, ...Object.values(filters)] as const,
};

export const projetoSocialEscolarKeys = {
  all: ["projeto-social-escolar"] as const,
  detail: (codigo_ue: string) => [...projetoSocialEscolarKeys.all, codigo_ue] as const,
  filters: (filters: Record<string, string | number>) => [...projetoSocialEscolarKeys.all, ...Object.values(filters)] as const,
};

export const dashboardKeys = {
  all: ["dashboard"] as const,
};