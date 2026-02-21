import { useGetAllSituacoes } from "@/core/apis/queries/situacao";
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

export function SituacaoSelect(props: Props) {
  const { data = [], isLoading } = useGetAllSituacoes();

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
      label={props.label || "Situação"}
      placeholder={props.placeholder || "Selecione a situação"}
      isLoading={isLoading}
      {...props}
    />
  );
}

export default SituacaoSelect
