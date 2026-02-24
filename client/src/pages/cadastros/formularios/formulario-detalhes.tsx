import React from "react";
import { useParams } from "react-router-dom";
import { Tabs, TabsContent } from "@/components/ui/tabs";
import { SidebarNav } from "@/components/ui/sidebar-nav";
import { Content } from "@/layouts/content";
import PageTitle from "@/components/commons/page-title";
import { FileText, TextCursorInput } from "lucide-react";
import { useGetFormularioDetalhes } from "@/core/apis/queries/formulario";
import { FormularioForm } from "./components/formulario-form";
import { PageSectionLayout } from "@/components/ui/page-section-layout";
import { Card, CardContent } from "@/components/ui/card";
import { CampoDetalhes } from "@/pages/formularios/campos/campo-detalhes";

export function FormularioDetalhes() {
  const sidebarNavItems = [
    { target: "dados", title: "Dados", icon: <FileText size={18} /> },
    { target: "campos", title: "Campos", icon: <TextCursorInput size={18} /> },
  ];

  const params = useParams();
  const id = params.id ? Number(params.id) : undefined;

  const { data, refetch } = useGetFormularioDetalhes(id ?? 0);
  const defaultValues = data?.data
    ? { ...data.data, id: Number(id) }
    : undefined;

  const [tabActive, setTabActive] = React.useState<string>(
    sidebarNavItems[0].target,
  );
  

  return (
    <Content>
      <PageTitle
        title="Cadastro de Formulário"
        desc="Gerencie as informações dos registros de formulários."
      />

      <Card className="p-4">
        <CardContent className="h-full p-0">
          <div className="flex h-full flex-col lg:flex-row lg:space-x-8">
            <aside className="w-full lg:w-1/5 lg:sticky lg:top-0">
              <SidebarNav
                items={sidebarNavItems as any}
                tabActive={tabActive}
                onSelect={(v) => setTabActive(v as string)}
              />
            </aside>

            <div className="flex-1 overflow-y-auto  py-2">
              <Tabs
                value={tabActive}
                onValueChange={setTabActive}
                className="flex-1 flex flex-col"
              >
                <TabsContent value="dados" className="w-full flex-1">
                  <div className="w-full h-full flex-1">
                    <PageSectionLayout
                      title="Dados"
                      desc="Gerencie os dados do formulário, como nome e slug."
                    >
                      <FormularioForm defaultValues={defaultValues} />
                    </PageSectionLayout>
                  </div>
                </TabsContent>
                <TabsContent value="campos" className="w-full flex-1">
                  <div className="w-full h-full flex-1">
                    <PageSectionLayout
                      title="Campos"
                      desc="Gerencie os campos do formulário."
                    >
                      <CampoDetalhes
                        formularioId={Number(id)}
                        toogleRefetch={refetch}
                        campos={
                          data?.data?.campos.map((c) => ({
                            ...c,
                            formulario_id: Number(id),
                          })) || []
                        }
                      />
                    </PageSectionLayout>
                  </div>
                </TabsContent>
              </Tabs>
            </div>
          </div>
        </CardContent>
      </Card>
    </Content>
  );
}
