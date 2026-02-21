import { get, post, remove, type ApiResult } from "./api";
import { URL_PROJETOS_SOCIAIS_ESCOLARES, URL_PROJETOS_SOCIAIS } from "../../constants/urls";
import type { ProjetoSocialEscolarDTO, ProjetoSocialEscolarRegistroDTO, ProjetoSocialPorCategoriaDTO, SalvarProjetoSocialEscolarDTO } from "../../dto/projeto-social-escolar-dto";
import { PaginationResponseDTO } from "@/core/dto/pagination-response-dto";


export const getProjetosSociaisEscolares = (filters?: Record<string, string | number>): Promise<ApiResult<PaginationResponseDTO<ProjetoSocialEscolarRegistroDTO>>> =>
  get(URL_PROJETOS_SOCIAIS_ESCOLARES, { params: filters });

export const getProjetoSocialEscolarDetalhes = (codigo_ue: string): Promise<ApiResult<ProjetoSocialEscolarDTO>> =>
  get(`${URL_PROJETOS_SOCIAIS_ESCOLARES}/${codigo_ue}/ue`);


export const getProjetosPorCategoria = (): Promise<ApiResult<ProjetoSocialPorCategoriaDTO[]>> =>
  get(`${URL_PROJETOS_SOCIAIS}/por-categoria`);


export const submitProjetoSocialEscolar = async (payload: SalvarProjetoSocialEscolarDTO) => {
  return post<SalvarProjetoSocialEscolarDTO>(URL_PROJETOS_SOCIAIS_ESCOLARES, payload)
}

export const excluirProjetoSocialEscolar = (id: number) =>
  remove(`${URL_PROJETOS_SOCIAIS_ESCOLARES}/${id}`);    
