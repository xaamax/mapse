import { requiredString } from "@/core/helpers/form-schemas-validators";
import { z } from "zod";

export const schema = z.object({
  slug: requiredString("Campo obrigatório."),
  nome: requiredString("Campo obrigatório."),
});

export type FormularioFormValues = z.infer<typeof schema>;

export const INITIAL_VALUES: FormularioFormValues = {
  slug: "",
  nome: "",
};
