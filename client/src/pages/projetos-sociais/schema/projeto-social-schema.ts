import { z } from "zod";

export const schema = z.object({
  nome: z.string({ required_error: "(*) Campo obrigatório" }),
  descricao: z.string({ required_error: "(*) Campo obrigatório" }),
  endereco: z.string({ required_error: "(*) Campo obrigatório" }),
  ativo: z.coerce.boolean({ required_error: "(*) Campo obrigatório" }),
  publico_alvo_id: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
  situacao_id: z.coerce.number({ required_error: "(*) Campo obrigatório" }),
});
export type ProjetoSocialFormValues = z.infer<typeof schema>;

export const INITIAL_VALUES: ProjetoSocialFormValues = {
  nome: "",
  descricao: "",
  endereco: "",
  ativo: true,
  publico_alvo_id: 0,
  situacao_id: 0,
};

export const ProjetoSocialSchema = schema;
