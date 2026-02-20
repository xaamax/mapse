import { useEffect } from "react";
import { useGetAllUesByDre } from "@/core/apis/queries/sme";
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

export function UeSelect(props: Props) {
  const dre = props.form.watch("dre");

  const { data = [], isLoading } = useGetAllUesByDre(dre ?? undefined);

  const ues =
    !props.hideSelectAll && dre === undefined
      ? data
      : [
          {
            value: undefined,
            label: "Todas",
          },
          ...data,
        ];

  useEffect(() => {
    if (!props.hideSelectAll && !dre) {
      props.form.setValue("ue", undefined);
    }
  }, [dre, props.form, props.hideSelectAll]);

  return (
    <SelectInput
      data={ues}
      label={props.label || "Unidade Educacional (UE)"}
      placeholder={props.placeholder || "Selecione a UE"}
      isLoading={isLoading}
      {...props}
    />
  );
}
