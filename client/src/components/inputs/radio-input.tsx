import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";

interface Props {
  label?: string;
  name: string;
  withAsterisk?: boolean;
  data: DataType[];
  form?: any;
}

function RadioInput({ label, name, data, withAsterisk = false, form }: Props) {
  return (
    <FormField
      control={form.control}
      name={name}
      render={({ field }) => (
        <FormItem className="space-y-3">
          {(label || withAsterisk) && (
            <FormLabel className="flex items-center gap-1">
              {withAsterisk && <span className="mt-1 text-destructive">*</span>}
              {label}{" "}
            </FormLabel>
          )}
          <FormControl>
            <RadioGroup
              onValueChange={(v) => {
                const parse = (val: string) => {
                  if (val === "true") return true;
                  if (val === "false") return false;
                  const n = Number(val);
                  if (!Number.isNaN(n) && String(n) === val) return n;
                  return val;
                };
                field.onChange(parse(v));
              }}
              value={field.value?.toString() ?? ""}
              className="flex space-y-1"
            >
              {data.map((d) => (
                <FormItem
                  key={String(d.value)}
                  className="flex items-center space-x-3 space-y-0"
                >
                  <FormControl>
                    <RadioGroupItem value={String(d.value)} />
                  </FormControl>
                  <FormLabel className="font-normal">{d.label}</FormLabel>
                </FormItem>
              ))}
            </RadioGroup>
          </FormControl>
          <FormMessage />
        </FormItem>
      )}
    />
  );
}

export default RadioInput;
