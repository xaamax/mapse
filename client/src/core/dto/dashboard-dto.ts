export interface DashboardDTO {
  indicadores: {
    title: string;
    value: number;
    icon: string;
  }[];
  projetos_sociais_categoria: {
    label: string;
    total: number;
  }[];
  projetos_sociais_dre: {
    label: string;
    total: number;
  }[];
  projetos_sociais_publico_alvo: {
    label: string;
    total: number;
  }[];
}
