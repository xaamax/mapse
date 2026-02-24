import { Form } from "@/components/ui/form";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  FormularioFormValues,
  INITIAL_VALUES,
  schema,
} from "../schemas/formulario-schema";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { FormularioDTO } from "@/core/dto/formulario-dto";
import TextInput from "@/components/inputs/text-input";
import { useNavigate } from "react-router-dom";
import { submitFormulario } from "@/core/apis/services/formulario-service";
import { toast } from "sonner";

interface FormProps {
  defaultValues?: FormularioDTO;
}

type SubmitAction = "save" | "save_add_other";

export function FormularioForm({ defaultValues }: FormProps) {
  const [submitAction, setSubmitAction] = useState<SubmitAction>("save");

  const navigate = useNavigate();

  const form = useForm<FormularioFormValues>({
    resolver: zodResolver(schema),
    shouldUnregister: false,
    defaultValues,
  });

  const { reset } = form;

  useEffect(() => {
    if (defaultValues) {
      reset(defaultValues);
    }
  }, [defaultValues, reset]);

  const onSubmit = async (data: FormularioFormValues) => {
    const formData = {
      ...(defaultValues?.id ? { ...data, id: defaultValues.id } : data),
    };

    return await submitFormulario(formData).then((response) => {
      if (response.success) {
        toast.success("Formulário salvo com sucesso!");

        if (submitAction === "save_add_other") {
          form.reset(INITIAL_VALUES);
          return;
        }
        navigate("/cadastros/formularios");
      }
    });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-6 px-12"
      >
        <TextInput
          label="Nome"
          placeholder="Digite o nome"
          name="nome"
          withAsterisk
          form={form}
        />
        <TextInput
          label="Slug"
          placeholder="Digite o slug"
          name="slug"
          withAsterisk
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
}
