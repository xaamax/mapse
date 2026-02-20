import type { AxiosResponse } from "axios";
import api from "./api";
import { closeAuth } from "@/core/hooks/use-auth-operations";

export const URL_REFRESH_TOKEN = "/v1/autenticacao/refresh-token";

interface AuthDTO {
  email: string;
  senha: string;
}

export interface AuthResponseDTO {
  access: string;
  refresh: string;
  expiresIn: string;
}

const login = (payload: AuthDTO): Promise<AxiosResponse<AuthResponseDTO>> =>
  api.post("/v1/autenticacao", { ...payload })

const refreshToken = (token: string): Promise<AxiosResponse> =>
  api.post("/v1/autenticacao/refresh-token", { token });

const logout = () => {
  closeAuth();
  window.location.href = "/login";
}

export default {
  refreshToken,
  login,
  logout,
};
