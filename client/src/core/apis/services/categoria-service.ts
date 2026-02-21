import { ApiResult, get } from "./api";
import { URL_CATEGORIAS } from "@/core/constants/urls";

export interface CategoriaDTO {
    id: number;
    nome: string;
}

export const getCategorias = (): Promise<ApiResult<CategoriaDTO[]>> =>
  get(`${URL_CATEGORIAS}/opcoes`);