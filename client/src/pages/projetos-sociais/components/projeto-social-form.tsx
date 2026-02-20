import { useForm } from "react-hook-form";
import { Form } from "@/components/ui/form";
import { zodResolver } from "@hookform/resolvers/zod";
import { ProjetoSocialDTO } from "@/core/dto/projeto-social-dto";
import { Button } from "@/components/ui/button";
import { submitProjetoSocial } from "@/core/apis/services/projeto-social-service";
import { DreSelect } from "@/components/selects/dre-select";
import { UeSelect } from "@/components/selects/ue-select";
import { toast } from "sonner";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ProjetoSocialFormValues, ProjetoSocialSchema } from "../schema/projeto-social-schema";
import { projetoSocialDtoToForm } from "../schema/projeto-social-form.adapter";
import Grid from "@/layouts/grid";

interface FormProps {
  defaultValues?: ProjetoSocialDTO;
}

type SubmitAction = "save" | "save_add_other";

export const ProjetoSocialForm = ({ defaultValues }: FormProps) => {
  const form = useForm<ProjetoSocialFormValues>({
    resolver: zodResolver(ProjetoSocialSchema),
    shouldUnregister: false,
    defaultValues
  });

  const [submitAction, setSubmitAction] = useState<SubmitAction>("save");

  const navigate = useNavigate();
  const { reset } = form;

  useEffect(() => {
    if (defaultValues) {
      reset(projetoSocialDtoToForm(defaultValues));
    }
  }, [defaultValues, reset]);

  const onSubmit = async (data: ProjetoSocialFormValues) => {
    const formData = {
      ...(defaultValues?.id ? { ...data, id: defaultValues.id } : data),
    };

    return await submitProjetoSocial(formData).then((response) => {
      if (response.success) {
        toast.success("Projeto social salvo com sucesso!");

        if (submitAction === "save_add_other") {
          form.reset({
                nome: "",
                descricao: "",
                endereco: "",
                publico_alvo: 0,
                situacao: 0,
                ativo: true,
                ue_id: 0,
          });
          return;
        }
        navigate("/projetos-sociais/consultar");
      }
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
            name="dre"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
          />
          <UeSelect
            name="ue"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
          />
        </Grid>
        <div className="flex justify-end gap-2">
          {!defaultValues?.id && (
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
