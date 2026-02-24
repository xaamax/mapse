import { CampoDetalhesDTO } from "./campo-dto";

export interface FormularioDTO {
    id: number;
    nome: string;
    slug: string;
}

export interface FormularioDetalhesDTO extends Omit<FormularioDTO, "id"> {
    campos: Omit<CampoDetalhesDTO, "formulario_id">[];
}

export interface SalvarFormularioDTO extends Omit<FormularioDTO, "id"> {
    id?: number;
}