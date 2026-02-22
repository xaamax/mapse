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
    dre_nome: string;
    dre_sigla: string;
    total_ues: number;
    total_projetos_escolares: number;
  }[];
  projetos_sociais_publico_alvo: {
    label: string;
    total: number;
  }[];
}
