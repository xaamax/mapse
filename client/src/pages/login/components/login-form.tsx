import { Form } from "@/components/ui/form";
import { toast } from "sonner";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema } from "../schemas/login-schema";
import TextInput from "@/components/inputs/text-input";
import PasswordInput from "@/components/inputs/password-input";
import { Button } from "@/components/ui/button";
import authService from "@/core/apis/services/auth-service";
import { setAuth } from "@/core/hooks/use-auth-operations";
import { useState } from "react";

type FormLoginValues = {
  email: string;
  senha: string;
};

export function LoginForm() {
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const form = useForm<FormLoginValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      senha: "",
    },
  });

  function onSubmit(values: FormLoginValues) {
    setIsLoading(true);
    authService.login(values)
      .then((response) => setAuth(response.data))
      .catch((error) => {
        setIsLoading(false)
        toast.error(error.response?.data?.messages || "Email ou senha inválidos");
      })
  }

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="rounded-lg p-4 space-y-4 w-full sm:w-[400px]"
      >
        <TextInput
          label="Email"
          placeholder="Digite seu email"
          name="email"
          withAsterisk
          form={form}
        />

        <PasswordInput
          label="Senha"
          placeholder="Digite sua senha"
          name="senha"
          withAsterisk
          form={form}
        />

        <Button type="submit" fullWidth disabled={isLoading}>
          {isLoading ? "Acessando..." : "Entrar"}
        </Button>
      </form>
    </Form>
  );
}
