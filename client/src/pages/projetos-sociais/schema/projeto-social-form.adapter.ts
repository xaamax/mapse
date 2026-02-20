import { ProjetoSocialDTO } from "@/core/dto/projeto-social-dto";
import { ProjetoSocialFormValues } from "./projeto-social-schema";

export function projetoSocialDtoToForm(
  dto: ProjetoSocialDTO
): ProjetoSocialFormValues {
  return {
    ...dto
  };
}
