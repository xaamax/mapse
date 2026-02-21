import { useGetAllCategorias } from "@/core/apis/queries/categoria";
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

export function CategoriaSelect(props: Props) {
  const { data = [], isLoading } = useGetAllCategorias();

  const options = props.hideSelectAll
    ? data
    : [
        {
          value: "",
          label: "Todas",
        },
        ...data,
      ];

  return (
    <SelectInput
      data={options}
      label={props.label || "Categoria"}
      placeholder={props.placeholder || "Selecione a categoria"}
      isLoading={isLoading}
      {...props}
    />
  );
}

export default CategoriaSelect
