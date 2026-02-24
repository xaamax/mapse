import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Textarea } from "@/components/ui/textarea";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  withAsterisk?: boolean;
  name: string;
  rows?: number;
  form?: any;
}

function TextareaInput({
  label,
  placeholder,
  description,
  withAsterisk = false,
  name,
  rows,
  form,
}: Props) {
  return (
    <FormField
      control={form.control}
      name={name}
      render={({ field }) => {
        const { value, onChange, onBlur, name: fieldName, ref, ...rest } = field;
        return (
          <FormItem>
            {(label || withAsterisk) && (
              <FormLabel className="flex items-center gap-1">
                {withAsterisk && (
                  <span className="mt-1 text-destructive">*</span>
                )}
                {label}{" "}
              </FormLabel>
            )}
            <FormControl>
              <Textarea
                placeholder={placeholder}
                className="resize-none"
                rows={rows}
                value={value ?? ""}
                onChange={onChange}
                onBlur={onBlur}
                name={fieldName}
                ref={ref}
                {...rest}
              />
            </FormControl>
            {description && <FormDescription>{description}</FormDescription>}
            <FormMessage />
          </FormItem>
        );
      }}
    />
  );
}

export default TextareaInput;
