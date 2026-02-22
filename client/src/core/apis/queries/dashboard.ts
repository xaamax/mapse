import { useQuery } from "@tanstack/react-query";
import dashboardService from "@/core/apis/services/dashboard-service";
import { dashboardKeys } from "./keys";

export function useGetDashboard(enabled: boolean = true) {
  return useQuery({
    queryKey: dashboardKeys.all,
    queryFn: () => dashboardService.getDashboard(),
    enabled,
  });
}
