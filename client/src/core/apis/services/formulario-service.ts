import { get, post, put, remove, type ApiResult } from "./api";
import { URL_FORMULARIOS } from "../../constants/urls";
import type { FormularioDetalhesDTO, FormularioDTO, SalvarFormularioDTO } from "../../dto/formulario-dto";
import { PaginationResponseDTO } from "@/core/dto/pagination-response-dto";


export const getFormularios = (filters?: Record<string, string | number>): Promise<ApiResult<PaginationResponseDTO<FormularioDTO>>> =>
  get(URL_FORMULARIOS, { params: filters });

export const getFormularioDetalhes = (id: number): Promise<ApiResult<FormularioDetalhesDTO>> =>
  get(`${URL_FORMULARIOS}/${id}/detalhes`);

export const getFormulariosOpcoes = (): Promise<ApiResult<FormularioDTO[]>> =>
  get(`${URL_FORMULARIOS}/opcoes-formularios`);

export const submitFormulario = async (payload: SalvarFormularioDTO) => {
  const url = payload.id ? `${URL_FORMULARIOS}/${payload.id}` : URL_FORMULARIOS;
  return !payload.id
    ? post<SalvarFormularioDTO>(url, payload)
    : put<SalvarFormularioDTO>(url, payload)
}

export const excluirFormulario = (id: number) =>
  remove(`${URL_FORMULARIOS}/${id}`);  