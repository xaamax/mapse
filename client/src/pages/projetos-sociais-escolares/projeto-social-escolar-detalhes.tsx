import PageTitle from "@/components/commons/page-title";
import { Content } from "@/layouts/content";
import { useParams } from "react-router-dom";
import { ProjetoSocialEscolarForm } from "./components/projeto-social-escolar-form";
import { useGetProjetoSocialEscolarPorUe } from "@/core/apis/queries/projeto-social-escolar";

export function ProjetoSocialEscolarDetalhes() {
  const { codigo_ue } = useParams();
  const { data } = useGetProjetoSocialEscolarPorUe(codigo_ue ?? "");

  return (
    <Content>
      <PageTitle
        title={`${codigo_ue ? "Editar" : "Incluir"} Projeto Social Escolar`}
        desc="Informações referentes ao registro de Projeto Social Escolar."
      />
      <ProjetoSocialEscolarForm defaultValues={data?.data || undefined } />
    </Content>
  );
}
