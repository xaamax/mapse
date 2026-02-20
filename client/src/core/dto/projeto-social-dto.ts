export interface ProjetoSocialRegistroDTO {
  id: number;
  nome: string;
  descricao: string;
  endereco: string;
  situacao: string;
}

export interface ProjetoSocialDTO {
    id: number,
    nome: string,
    descricao: string,
    endereco: string,
    publico_alvo: number,
    situacao: number,
    ativo: boolean,
    ue_id: number,
}

export interface SalvarProjetoSocialDTO extends Omit<ProjetoSocialDTO, "id"> {
    id?: number;
} 