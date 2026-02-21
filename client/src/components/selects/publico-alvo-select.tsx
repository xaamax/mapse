import { useGetAllPublicosAlvos } from "@/core/apis/queries/publico-alvo";
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
}

export function PublicoAlvoSelect(props: Props) {
  const { data = [], isLoading } = useGetAllPublicosAlvos();

  const options = props.hideSelectAll
    ? data
    : [
        {
          value: undefined,
          label: "Todas",
        },
        ...data,
      ];

  return (
    <SelectInput
      data={options}
      label={props.label || "Público alvo"}
      placeholder={props.placeholder || "Selecione o público alvo"}
      isLoading={isLoading}
      {...props}
    />
  );
}

export default PublicoAlvoSelect
