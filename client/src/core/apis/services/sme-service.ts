import { ApiResult, get } from "./api";
import { URL_DRES, URL_UES } from "@/core/constants/urls";

export interface DreDTO {
    codigo_dre: string;
    nome: string;
}

export interface UeDTO {
    id: number;
    codigo_ue: string;
    nome: string;
}

export const getDres = (): Promise<ApiResult<DreDTO[]>> =>
  get(`${URL_DRES}/codigos-nomes`);

export const getUesPorDre = (codigo_dre: string): Promise<ApiResult<UeDTO[]>> =>
  get(`${URL_UES}/por-dre/${codigo_dre}`);