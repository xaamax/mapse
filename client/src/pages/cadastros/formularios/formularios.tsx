import { Content } from "@/layouts/content";
import PageTitle from "@/components/commons/page-title";
import { Button } from "@/components/ui/button";
import { PlusCircle } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useGetAllFormularios } from "@/core/apis/queries/formulario";
import Box from "@/widgets/box";
import Grid from "@/layouts/grid";
import { RowActions } from "./components/row-actions";

export function Formularios() {
  const navigate = useNavigate();
  const { data } = useGetAllFormularios({
    page_number: 1,
    page_size: 10,
  });

  return (
    <Content>
      <PageTitle
        title="Formulários"
        desc="Gerencie os cadastros de formulários."
        actions={
          <Button
            variant="ghost_primary"
            onClick={() => navigate("/cadastros/formularios/incluir")}
          >
            <PlusCircle className="mr-2 h-5 w-5" />
            Adicionar Formulário
          </Button>
        }
      />
      <Grid lg={4} md={4}>
        {data?.data?.items.map((formulario) => (
          <Box
            key={formulario.id}
            title={`#${formulario.id}`}
            actions={
              <Link
                to={`/cadastros/formularios/${formulario.id}`}
                className="text-primary"
              >
                <RowActions row={formulario} />
              </Link>
            }
          >
            <p className="font-light">{formulario.nome}</p>
            <small className="font-medium !text-gray-400">
              {formulario.slug}
            </small>
          </Box>
        ))}
      </Grid>
    </Content>
  );
}
