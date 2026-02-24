export interface CampoDTO {
  id: number;
  nome: string;
  label: string;
  observacao?: string | null;
  ordem: number;
  tipo: number;
  opcional?: string | null;
  xs?: number | null;
  lg?: number | null;
  md?: number | null;
  sm?: number | null;
  readonly?: boolean;
  tamanho?: number | null;
  mascara?: string | null;
  placeholder?: string | null;
  formulario_id: number;
}

export interface CampoDetalhesDTO extends CampoDTO {
  tipo_campo: string;
}

export interface SalvarCampoDTO extends Omit<CampoDTO, "id"> {
  id?: number;
}