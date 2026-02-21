import { z } from "zod";

export const schema = z.object({
  ue_id: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  projetos_sociais: z.array(z.number()).min(1, "(*) Campo obrigatório"),
});
export type ProjetoSocialEscolarFormValues = z.infer<typeof schema>;

export const INITIAL_VALUES: ProjetoSocialEscolarFormValues = {
  ue_id: undefined as unknown as number,
  projetos_sociais: [],
};

export const ProjetoSocialEscolarSchema = schema;
