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
    publico_alvo_id: number,
    situacao_id: number,
    ativo: boolean,
}

export interface SalvarProjetoSocialDTO extends Omit<ProjetoSocialDTO, "id"> {
    id?: number;
} 