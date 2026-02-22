import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { Form } from "@/components/ui/form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import {
  submitProjetoSocialEscolar,
  getProjetosPorCategoria,
  getProjetoSocialEscolarExisteUe,
} from "@/core/apis/services/projeto-social-escolar-service";
import { Card, CardHeader, CardContent, CardTitle } from "@/components/ui/card";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";
import {
  INITIAL_VALUES,
  ProjetoSocialEscolarFormValues,
  ProjetoSocialEscolarSchema,
} from "../schema/projeto-social-escolar-schema";
import Grid from "@/layouts/grid";
import { DreSelect } from "@/components/selects/dre-select";
import { UeSelect } from "@/components/selects/ue-select";
import {
  ProjetoSocialEscolarDTO,
  ProjetoSocialPorCategoriaDTO,
} from "@/core/dto/projeto-social-escolar-dto";
import { ChevronDownCircle, ChevronUpCircle } from "lucide-react";
import { Badge } from "@/components/ui/badge";

type SubmitAction = "save" | "save_add_other";

interface FormProps {
  defaultValues?: ProjetoSocialEscolarDTO;
}

export const ProjetoSocialEscolarForm = ({ defaultValues }: FormProps) => {
  const form = useForm<ProjetoSocialEscolarFormValues>({
    resolver: zodResolver(ProjetoSocialEscolarSchema),
    mode: "onChange",
    defaultValues,
  });

  const [categorias, setCategorias] = useState<ProjetoSocialPorCategoriaDTO[]>(
    [],
  );
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  const [submitAction, setSubmitAction] = useState<SubmitAction>("save");

  const navigate = useNavigate();
  const { reset } = form;

  useEffect(() => {
    if (defaultValues) {
      reset(defaultValues);
    }
  }, [defaultValues, reset]);

  const onSubmit = async (data: ProjetoSocialEscolarFormValues) => {
    return await submitProjetoSocialEscolar(data).then((response) => {
      if (response.success) {
        toast.success("Projeto social salvo com sucesso!");

        if (submitAction === "save_add_other") {
          form.reset(INITIAL_VALUES);
          return;
        }
        navigate("/projetos-sociais-escolares");
      }
    });
  };

  const [existeRegistro, setExisteRegistro] = useState<boolean>(false);

  useEffect(() => {
    getProjetosPorCategoria().then((res) => {
      if (!form.getValues("ue_id")) return;
      if (res.success) {
        getProjetoSocialEscolarExisteUe(form.getValues("ue_id")).then((res) => {
          setExisteRegistro(!!res.data);
        });
        setCategorias(res.data ?? []);
      }
    });
  }, [form.getValues("ue_id")]);

  const isEditMode = Boolean(defaultValues);

  const toggleCategory = (name: string) => {
    setExpanded((s) => ({ ...s, [name]: !s[name] }));
  };

  const toggleProject = (id: number, checked?: boolean) => {
    const current: number[] = form.getValues("projetos_sociais") || [];
    let next: number[];
    if (typeof checked === "boolean") {
      next = checked
        ? Array.from(new Set([...current, id]))
        : current.filter((x) => x !== id);
    } else {
      const exists = current.includes(id);
      next = exists ? current.filter((x) => x !== id) : [...current, id];
    }

    form.setValue("projetos_sociais", next, {
      shouldValidate: true,
      shouldDirty: true,
    });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-6 px-12 pt-4"
      >
        <Grid cols="12 2 2 2">
          <DreSelect
            name="codigo_dre"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
            disabled={isEditMode}
          />

          <UeSelect
            name="ue_id"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
            disabled={isEditMode}
          />
        </Grid>
        <div className="space-y-3">
          {existeRegistro ? (
            <Badge variant="warning" className="w-full text-1xl font-light">
              <h1>Já existe Projeto Social Escolar para esta UE.</h1>
            </Badge>
          ) : (
            categorias.map((cat) => (
              <Card key={cat.categoria}>
                <CardHeader
                  className="flex items-center cursor-pointer"
                  onClick={() => toggleCategory(cat.categoria)}
                >
                  <div className="flex text-primary justify-between w-full">
                    <CardTitle>{cat.categoria}</CardTitle>
                    <div className="ml-2">
                      {expanded[cat.categoria] ? (
                        <ChevronUpCircle />
                      ) : (
                        <ChevronDownCircle />
                      )}
                    </div>
                  </div>
                </CardHeader>
                {expanded[cat.categoria] && (
                  <CardContent>
                    <div className="flex flex-col gap-2">
                      {cat.projetos_sociais.map((p) => (
                        <label key={p.id} className="flex items-center gap-3">
                          <Checkbox
                            checked={(
                              form.getValues("projetos_sociais") || []
                            ).includes(p.id)}
                            onCheckedChange={(checked) =>
                              toggleProject(p.id, Boolean(checked))
                            }
                          />
                          <div>
                            <div className="font-medium">{p.nome}</div>
                            <div className="text-sm text-muted-foreground">
                              {p.descricao}
                            </div>
                          </div>
                        </label>
                      ))}
                    </div>
                  </CardContent>
                )}
              </Card>
            ))
          )}
        </div>
        <div className="flex justify-end gap-2">
          {!isEditMode && (
            <Button
              type="submit"
              variant="outline_primary"
              disabled={!form.formState.isValid}
              onClick={() => setSubmitAction("save_add_other")}
            >
              Salvar e incluir outro
            </Button>
          )}
          <Button
            type="submit"
            disabled={!form.formState.isValid}
            onClick={() => setSubmitAction("save")}
          >
            Salvar
          </Button>
        </div>
      </form>
    </Form>
  );
};
