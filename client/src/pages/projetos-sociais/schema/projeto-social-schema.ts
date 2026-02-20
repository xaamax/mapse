import { z } from "zod";

export const schema = z.object({
  nome: z.string({ required_error: "(*) Campo obrigatório" }),
  descricao: z.string({ required_error: "(*) Campo obrigatório" }),
  endereco: z.string({ required_error: "(*) Campo obrigatório" }),
  publico_alvo: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  situacao: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  ue_id: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
});
export type projetoSocialFormValues = z.infer<typeof schema>;

export const projetoSocialSchema = z.array(schema);