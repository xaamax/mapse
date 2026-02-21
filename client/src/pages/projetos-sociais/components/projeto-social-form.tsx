import { useForm } from "react-hook-form";
import { Form } from "@/components/ui/form";
import { zodResolver } from "@hookform/resolvers/zod";
import { ProjetoSocialDTO } from "@/core/dto/projeto-social-dto";
import { Button } from "@/components/ui/button";
import { submitProjetoSocial } from "@/core/apis/services/projeto-social-service";
import { toast } from "sonner";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  INITIAL_VALUES,
  ProjetoSocialFormValues,
  ProjetoSocialSchema,
} from "../schema/projeto-social-schema";
import { projetoSocialDtoToForm } from "../schema/projeto-social-form.adapter";
import Grid from "@/layouts/grid";
import TextInput from "@/components/inputs/text-input";
import TextareaInput from "@/components/inputs/textarea-input";
import SituacaoSelect from "@/components/selects/situacao-select";
import PublicoAlvoSelect from "@/components/selects/publico-alvo-select";

interface FormProps {
  defaultValues?: ProjetoSocialDTO;
}

type SubmitAction = "save" | "save_add_other";

export const ProjetoSocialForm = ({ defaultValues }: FormProps) => {
  const form = useForm<ProjetoSocialFormValues>({
    resolver: zodResolver(ProjetoSocialSchema),
    shouldUnregister: false,
    defaultValues,
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
          form.reset(INITIAL_VALUES);
          return;
        }
        navigate("/projetos-sociais");
      }
    });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-6 px-12 pt-4"
      >
        <TextInput
          label="Nome do projeto social"
          placeholder="Digite o nome do projeto social"
          name="nome"
          withAsterisk
          form={form}
        />
        <TextInput
          label="Endereço do projeto social"
          placeholder="Digite o endereço do projeto social"
          name="endereco"
          withAsterisk
          form={form}
        />
        <Grid cols="12 2 2 2">
          <PublicoAlvoSelect
            name="publico_alvo_id"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
          />
          <SituacaoSelect
            name="situacao_id"
            form={form}
            withAsterisk={true}
            hideSelectAll={true}
          />
        </Grid>
        <TextareaInput
          label="Descrição do projeto social"
          placeholder="Descreva as informações do projeto social"
          name="descricao"
          withAsterisk
          rows={5}
          form={form}
        />
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
