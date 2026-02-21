import PageTitle from "@/components/commons/page-title";
import { Content } from "@/layouts/content";
import { useParams } from "react-router-dom";
import { ProjetoSocialForm } from "./components/projeto-social-form";
import { useGetProjetoSocialPorId } from "@/core/apis/queries/projeto-social";

export function ProjetoSocialDetalhes() {
  const { id } = useParams();
  const { data } = useGetProjetoSocialPorId(Number(id));
  const defaultValues = data?.data
    ? { ...data.data, id: Number(id) }
    : undefined;

  return (
    <Content>
      <PageTitle
        title={`${id ? "Editar" : "Incluir"} Projeto Social`}
        desc="Informações referentes ao registro de Projeto Social."
      />
      <ProjetoSocialForm {...{ defaultValues }} />
    </Content>
  );
}
