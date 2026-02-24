import { useState } from "react";
import { Content } from "@/layouts/content";
import { CampoForm } from "./components/campo-form";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { CampoDetalhesDTO } from "@/core/dto/campo-dto";
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { RowActions } from "./components/row-actions";
import { INITIAL_VALUES } from "./schemas/campo-schema";
import { Badge } from "@/components/ui/badge";

type Props = {
  formularioId: number;
  campos: CampoDetalhesDTO[];
  toogleRefetch: () => void;
};

export function CampoDetalhes({ campos, formularioId, toogleRefetch }: Props) {
  const [tabs, setTabs] = useState([
    { title: "Visão Geral", target: "visao-geral" },
    { title: "Incluir Campo", target: "cadastro" },
  ]);

  const [tabActive, setTabActive] = useState<string>(tabs[0].target);
  const [defaultValues, setDefaultValues] = useState<CampoDetalhesDTO>({
    ...INITIAL_VALUES,
    formulario_id: formularioId,
  } as CampoDetalhesDTO);

  const handleClickEdit = (campo: CampoDetalhesDTO) => {
    setTabActive("cadastro");
    setDefaultValues(campo);

    setTabs((prev) => {
      const exists = prev.some((t) => t.target === "cadastro");

      if (exists) {
        return prev.map((t) =>
          t.target === "cadastro" ? { ...t, title: "Editar Campo" } : t,
        );
      }

      return [...prev, { target: "cadastro", title: "Editar Campo" }];
    });
  };

  const handleTabsChange = (value: string) => {
    setTabActive(value);

    setTabs((prev) =>
      prev.map((t) =>
        t.target === "cadastro" ? { ...t, title: "Incluir Campo" } : t,
      ),
    );

    setDefaultValues({
      ...INITIAL_VALUES,
      formulario_id: formularioId,
    } as CampoDetalhesDTO);

    if (value === "visao-geral") toogleRefetch();
  };

  return (
    <Content>
      <Tabs value={tabActive} onValueChange={handleTabsChange}>
        <TabsList>
          {tabs.map((tab, idx) => (
            <TabsTrigger key={idx} value={tab.target}>
              {tab.title}
            </TabsTrigger>
          ))}
        </TabsList>
        <TabsContent value="visao-geral" className="space-y-3 mt-4">
          {!campos.length ? (
            <div>Nenhum campo encontrado.</div>
          ) : (
            <>
              {campos.map((campo) => (
                <Card key={campo.id}>
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle>
                        #{campo.ordem} {campo.label}
                      </CardTitle>
                      <RowActions row={campo} onClickEdit={handleClickEdit} />
                    </div>
                    <div className="flex flex-0 flex-col space-y-1">
                      <div>
                        <Badge>{campo.tipo_campo}</Badge>
                      </div>
                    </div>
                  </CardHeader>
                </Card>
              ))}
            </>
          )}
        </TabsContent>
        <TabsContent value="cadastro">
          <CampoForm
            defaultValues={defaultValues}
            onSave={() => handleTabsChange("visao-geral")}
          />
        </TabsContent>
      </Tabs>
    </Content>
  );
}
