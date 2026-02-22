import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type Props = {
  data: { dre_nome: string; dre_sigla: string; total_ues: number, total_projetos_escolares: number }[];
};

export function ChartProjetosSociaisDre({ data }: Props) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Projetos Sociais por DRE</CardTitle>
        <CardDescription>Total de projetos sociais por DRE</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-8">
          {data.map((item, idx) => (
            <div className="flex items-center" key={idx}>
              <Avatar className="h-9 w-9">
                <AvatarImage src="/avatars/01.png" alt="Avatar" />
                <AvatarFallback>{item.dre_sigla}</AvatarFallback>
              </Avatar>
              <div className="ml-4 space-y-1">
                <p className="text-sm font-medium leading-none">
                  {item.dre_nome}
                </p>
                <p className="text-sm text-muted-foreground">
                  Unidades Educacionais Atendidas: {item.total_ues}
                </p>
              </div>
              <div className="ml-auto font-medium text-2xl">{item.total_projetos_escolares}</div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
