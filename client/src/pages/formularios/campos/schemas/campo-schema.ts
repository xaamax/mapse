import { requiredString } from "@/core/helpers/form-schemas-validators";
import { z } from "zod";

export const schema = z.object({
    nome: requiredString("O nome é obrigatório"),
    label: requiredString("O label é obrigatório"),
    observacao: z.string().optional().nullable(),
    ordem: z.coerce.number({ required_error: "A ordem é obrigatória" }),
    tipo: z.coerce.number({ required_error: "O tipo é obrigatório" }),
    opcional: z.string().optional().nullable(),    
    xs: z.coerce.number().optional().nullable(),
    lg: z.coerce.number().optional().nullable(),
    md: z.coerce.number().optional().nullable(),
    sm: z.coerce.number().optional().nullable(),
    readonly: z.coerce.boolean({ required_error: "O campo somente leitura é obrigatório" }),
    tamanho: z.coerce.number().optional().nullable(),
    mascara: z.string().optional().nullable(),
    placeholder: z.string().optional().nullable(), 
    formulario_id: z.coerce.number({ required_error: "O formulário é obrigatório" }),
});

export type FormValues = z.infer<typeof schema>;

export const INITIAL_VALUES: FormValues = {
  nome: "",
  label: "",
  observacao: undefined as unknown as string,
  ordem: undefined as unknown as number,
  tipo: undefined as unknown as number,
  opcional: undefined as unknown as string,
  xs: undefined as unknown as number,
  lg: undefined as unknown as number,
  md: undefined as unknown as number,
  sm: undefined as unknown as number,
  readonly: false,
  tamanho: undefined as unknown as number,
  mascara: undefined as unknown as string,
  placeholder: undefined as unknown as string,
  formulario_id: undefined as unknown as number,
};
