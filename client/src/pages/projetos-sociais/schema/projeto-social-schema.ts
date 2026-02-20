import { z } from "zod";

export const schema = z.object({
  nome: z.string({ required_error: "(*) Campo obrigatório" }),
  descricao: z.string({ required_error: "(*) Campo obrigatório" }),
  endereco: z.string({ required_error: "(*) Campo obrigatório" }),
  publico_alvo: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  situacao: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  ativo: z.coerce.boolean({ required_error: "(*) Campo obrigatório" }),
  ue_id: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
});
export type ProjetoSocialFormValues = z.infer<typeof schema>;

export const ProjetoSocialSchema = z.array(schema);