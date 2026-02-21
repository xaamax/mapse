export interface ProjetoSocialDTO {
    id: number,
    nome: string,
    descricao: string,
    endereco: string,
    publico_alvo_id: number,
    categoria_id: number,
    ativo: boolean,
}

export interface ProjetoSocialRegistroDTO {
  id: number;
  nome: string;
  descricao: string;
  endereco: string;
  categoria_nome: string;
  publico_alvo_nome: string;
}

export interface SalvarProjetoSocialDTO extends Omit<ProjetoSocialDTO, "id"> {
    id?: number;
} 