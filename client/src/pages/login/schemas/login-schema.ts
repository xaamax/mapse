import { requiredString } from "@/core/helpers/form-schemas-validators";
import { z } from "zod";

export const loginSchema = z.object({
  email: requiredString("Campo obrigatório."),
  senha: requiredString("Campo obrigatório."),
});
