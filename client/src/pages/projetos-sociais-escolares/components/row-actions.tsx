import { DotsVerticalIcon } from "@radix-ui/react-icons";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Search } from "lucide-react";
import { Link } from "react-router-dom";
import { ProjetoSocialEscolarRegistroDTO } from "@/core/dto/projeto-social-escolar-dto";

type Props = {
  row: ProjetoSocialEscolarRegistroDTO;
  toogleRefreshTable?: () => void;
};

export function DataTableRowActions({ row }: Props) {

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="ghost"
          className="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
        >
          <DotsVerticalIcon className="h-4 w-4" />
          <span className="sr-only">Abrir menu</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-[160px]">
        <Link to={`/projetos-sociais-escolares/${row?.codigo_ue}/ue`}>
          <DropdownMenuItem>
            Consultar
            <DropdownMenuShortcut>
              <Search className="h-4 w-4" />
            </DropdownMenuShortcut>
          </DropdownMenuItem>
        </Link>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
