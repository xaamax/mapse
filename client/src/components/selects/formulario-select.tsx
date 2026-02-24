import { useGetFormulariosOpcoes } from "@/core/apis/queries/formulario";
import SelectInput from "@/components/inputs/select-input";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  withAsterisk?: boolean;
  name: string;
  form?: any;
  isLoading?: boolean;
  className?: string;
  hideSelectAll?: boolean;
  disabled?: boolean;
}

export function FormularioSelect(props: Props) {
  const { data = [], isLoading } = useGetFormulariosOpcoes();

  return (
    <SelectInput
      key={`formulario-select-${props.form.getValues("formulario_id")}`}
      data={data}
      label={props.label || "Formulário"}
      placeholder={props.placeholder || "Selecione o formulário"}
      isLoading={isLoading}
      {...props}
    />
  );
}

export default FormularioSelect;
