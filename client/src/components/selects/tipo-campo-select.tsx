import { useGetAllCamposTipos } from "@/core/apis/queries/campo";
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

export function TipoCampoSelect(props: Props) {
  const { data = [], isLoading } = useGetAllCamposTipos();

  return (
    <SelectInput
      key={`tipo-campo-select-${props.form.getValues("tipo")}`}
      data={data}
      label={props.label || "Tipo de Campo"}
      placeholder={props.placeholder || "Selecione o tipo de campo"}
      isLoading={isLoading}
      {...props}
    />
  );
}

export default TipoCampoSelect;
