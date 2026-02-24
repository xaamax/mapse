import { Form } from "@/components/ui/form";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { FormValues, INITIAL_VALUES, schema } from "../schemas/campo-schema";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { CampoDTO } from "@/core/dto/campo-dto";
import TextInput from "@/components/inputs/text-input";
import Grid from "@/layouts/grid";
import { submitCampo } from "@/core/apis/services/campo-service";
import { toast } from "sonner";
import TextareaInput from "@/components/inputs/textarea-input";
import RadioInput from "@/components/inputs/radio-input";
import FormularioSelect from "@/components/selects/formulario-select";
import TipoCampoSelect from "@/components/selects/tipo-campo-select";

interface FormProps {
  defaultValues?: CampoDTO;
  onSave?: () => void;
}

type SubmitAction = "save" | "save_add_other";

export function CampoForm({ defaultValues, onSave }: FormProps) {
  const [submitAction, setSubmitAction] = useState<SubmitAction>("save");

  const form = useForm<FormValues>({
    resolver: zodResolver(schema),
    shouldUnregister: false,
    defaultValues,
  });

  const { reset } = form;

  useEffect(() => {
    if (form.getValues("readonly") === undefined)
      form.setValue("readonly", false);

    if (defaultValues) {
      reset(defaultValues);
    }
  }, [defaultValues, reset, form]);

  const onSubmit = async (data: FormValues) => {
    const formData = {
      ...(defaultValues?.id ? { ...data, id: defaultValues.id } : data),
    };

    return await submitCampo(formData).then((response) => {
      if (response.success) {
        toast.success("Campo salvo com sucesso!");

        if (submitAction === "save_add_other") {
          form.reset(INITIAL_VALUES);
          return;
        }
        onSave?.();
      }
    });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-6 px-1 mt-4"
      >
        <FormularioSelect
          name="formulario_id"
          form={form}
          disabled={true}
          withAsterisk={true}
          hideSelectAll={true}
        />
        <Grid lg={2} md={2}>
          <TextInput
            label="Label"
            placeholder="Digite o label"
            name="label"
            withAsterisk
            form={form}
          />
          <TextInput
            label="Nome"
            placeholder="Digite o nome"
            name="nome"
            withAsterisk
            form={form}
          />
          <TextInput
            label="Placeholder"
            placeholder="Digite o placeholder"
            name="placeholder"
            form={form}
          />
          <TextInput
            label="Máscara"
            placeholder="Digite a máscara"
            name="mascara"
            form={form}
          />
        </Grid>
        <Grid lg={4} md={4}>
          <TextInput
            label="Ordem"
            placeholder="Digite a ordem"
            name="ordem"
            withAsterisk
            type="number"
            form={form}
          />
          <TipoCampoSelect label="Tipo" name="tipo" withAsterisk form={form} />
          <TextInput
            label="Tamanho"
            placeholder="Digite o tamanho"
            name="tamanho"
            type="number"
            form={form}
          />
          <RadioInput
            label="Somente leitura"
            name="readonly"
            data={[
              { label: "Sim", value: "true" },
              { label: "Não", value: "false" },
            ]}
            withAsterisk
            form={form}
          />
          <TextInput
            label="xs (<=576px)"
            placeholder="Digite a resolução em xs"
            name="xs"
            type="number"
            form={form}
          />
          <TextInput
            label="sm (<=768px)"
            placeholder="Digite a resolução em sm"
            name="sm"
            type="number"
            form={form}
          />
          <TextInput
            label="md (<=992px)"
            placeholder="Digite a resolução em md"
            name="md"
            type="number"
            form={form}
          />
          <TextInput
            label="lg (<=1200px)"
            placeholder="Digite a resolução em lg"
            name="lg"
            type="number"
            form={form}
          />
        </Grid>
        <TextareaInput
          label="Opcional"
          placeholder="Digite o opcional"
          name="opcional"
          rows={4}
          form={form}
        />
        <TextareaInput
          label="Observação"
          placeholder="Digite a observação"
          name="observacao"
          rows={4}
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
