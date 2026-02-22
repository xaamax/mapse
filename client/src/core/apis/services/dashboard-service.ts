import { get, type ApiResult } from "./api";
import { URL_DASHBOARD } from "../../constants/urls";
import type { DashboardDTO } from "../../dto/dashboard-dto";

export const getDashboard = (): Promise<ApiResult<DashboardDTO>> =>
  get(URL_DASHBOARD);

export default {
  getDashboard,
};
