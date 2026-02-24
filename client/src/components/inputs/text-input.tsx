import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  withAsterisk?: boolean;
  name: string;
  form?: any;
  type?: string;
}

function TextInput({
  label,
  placeholder,
  description,
  withAsterisk = false,
  name,
  form,
  type = "text",  
}: Props) {
  return (
    <FormField
      control={form.control}
      name={name}
      render={({ field }) => (
        <FormItem>
          {(label || withAsterisk) && (
            <FormLabel className="flex items-center mt-1 gap-1">
              {withAsterisk && <span className="text-destructive">*</span>}
              {label}{" "}
            </FormLabel>
          )}
          <FormControl>
            <Input placeholder={placeholder} type={type} {...field} />
          </FormControl>

          {description && <FormDescription>{description}</FormDescription>}
          <FormMessage />
        </FormItem>
      )}
    />
  );
}

export default TextInput;
