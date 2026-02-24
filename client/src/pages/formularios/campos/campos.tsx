import { Content } from "@/layouts/content";
import PageTitle from "@/components/commons/page-title";
import { Button } from "@/components/ui/button";
import { PlusCircle } from "lucide-react";
import { useNavigate } from "react-router-dom";

export function Campos() {
  const navigate = useNavigate();
  return (
    <Content>
      <PageTitle
        title="Campos"
        desc="Gerencie os cadastros de campos dos formulários."
        actions={
          <Button
            variant="ghost_primary"
            onClick={() => navigate("/formularios/campos/incluir")}
          >
            <PlusCircle className="mr-2 h-5 w-5" />
            Adicionar Campo
          </Button>
        }
      />
    </Content>
  );
}
