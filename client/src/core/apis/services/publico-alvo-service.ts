import { ApiResult, get } from "./api";
import { URL_PUBLICOS_ALVOS } from "@/core/constants/urls";

export interface PublicoAlvoDTO {
    id: number;
    nome: string;
}

export const getPublicosAlvos = (): Promise<ApiResult<PublicoAlvoDTO[]>> =>
  get(`${URL_PUBLICOS_ALVOS}/opcoes`);