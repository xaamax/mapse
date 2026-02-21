export interface ProjetoSocialEscolarRegistroDTO {
  codigo_ue: string;
  ue_nome: string;
  dre_nome: string;
  projeto_social_nome: string;
}

export interface ProjetoSocialPorCategoriaDTO {
  categoria: string;
  projetos_sociais: Array<{
    id: number;
    nome: string;
    descricao: string;
  }>;
}

export interface ProjetoSocialEscolarDTO {
  codigo_dre: string;
  ue_id: number;
  projetos_sociais: number[];
} 

export interface SalvarProjetoSocialEscolarDTO extends Omit<ProjetoSocialEscolarDTO, "codigo_dre"> {}