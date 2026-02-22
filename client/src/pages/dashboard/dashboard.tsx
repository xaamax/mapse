import { Content } from "@/layouts/content";
import { useGetDashboard } from "@/core/apis/queries/dashboard";
import PageTitle from "@/components/commons/page-title";
import BoxValue from "@/widgets/box-value";
import ICONS from "@/core/icons";
import type { ElementType } from "react";
import Grid from "@/layouts/grid";

export function Dashboard() {
  const { data } = useGetDashboard();

  return (
    <Content>
      <PageTitle
        title="Dashboard"
        desc="Visão Geral dos Projetos Sociais Escolares."
        hideToBack
      />
      <Grid lg={4} md={4}>
        {data?.data?.indicadores?.map((indicador, idx) => {
          const Icon = (ICONS[indicador.icon as keyof typeof ICONS] ??
            ICONS.Activity) as ElementType;
          return (
            <BoxValue
              key={idx}
              title={indicador.title}
              value={indicador.value}
              icon={Icon}
            />
          );
        })}
      </Grid>
    </Content>
  );
}
