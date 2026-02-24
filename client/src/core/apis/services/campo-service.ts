import { get, post, put, remove, type ApiResult } from "./api";
import { URL_CAMPOS } from "../../constants/urls";
import type { CampoDTO, SalvarCampoDTO } from "../../dto/campo-dto";
import { PaginationResponseDTO } from "@/core/dto/pagination-response-dto";


export const getCampos = (filters?: Record<string, string | number>): Promise<ApiResult<PaginationResponseDTO<CampoDTO>>> =>
  get(URL_CAMPOS, { params: filters });

export const getCampoDetalhes = (id: number): Promise<ApiResult<CampoDTO>> =>
  get(`${URL_CAMPOS}/${id} `);

export const getCamposFormulario = (formulario_id: number): Promise<ApiResult<CampoDTO[]>> =>
  get(`${URL_CAMPOS}/formulario/${formulario_id}`);

export const getCamposTipos = (): Promise<ApiResult<{ label: string; value: number }[]>> =>
  get(`${URL_CAMPOS}/tipos`);

export const submitCampo = async (payload: SalvarCampoDTO) => {
  const url = payload.id ? `${URL_CAMPOS}/${payload.id}` : URL_CAMPOS;
  return !payload.id
    ? post<SalvarCampoDTO>(url, payload)
    : put<SalvarCampoDTO>(url, payload)
}

export const excluirCampo = (id: number) =>
  remove(`${URL_CAMPOS}/${id}`);  