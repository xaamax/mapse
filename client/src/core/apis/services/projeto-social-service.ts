import { get, post, put, remove, type ApiResult } from "./api";
import { URL_PROJETOS_SOCIAIS } from "../../constants/urls";
import type { SalvarProjetoSocialDTO, ProjetoSocialDTO, ProjetoSocialRegistroDTO } from "../../dto/projeto-social-dto";
import { PaginationResponseDTO } from "@/core/dto/pagination-response-dto";


export const getProjetosSociais = (filters?: Record<string, string | number>): Promise<ApiResult<PaginationResponseDTO<ProjetoSocialRegistroDTO>>> =>
  get(URL_PROJETOS_SOCIAIS, { params: filters });

export const getProjetoSocialDetalhes = (id: number): Promise<ApiResult<ProjetoSocialDTO>> =>
  get(`${URL_PROJETOS_SOCIAIS}${id}`);


export const submitProjetoSocial = async (payload: SalvarProjetoSocialDTO) => {
  const url = payload.id ? `${URL_PROJETOS_SOCIAIS}${payload.id}` : URL_PROJETOS_SOCIAIS;
  return !payload.id
    ? post<SalvarProjetoSocialDTO>(url, payload)
    : put<SalvarProjetoSocialDTO>(url, payload)
}

export const excluirProjetoSocial = (id: number) =>
  remove(`${URL_PROJETOS_SOCIAIS}${id}`);    
