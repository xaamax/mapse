import { ApiResult, get } from "./api";
import { URL_SITUACOES } from "@/core/constants/urls";

export interface SituacaoDTO {
    id: number;
    nome: string;
}

export const getSituacoes = (): Promise<ApiResult<SituacaoDTO[]>> =>
  get(`${URL_SITUACOES}/opcoes`);