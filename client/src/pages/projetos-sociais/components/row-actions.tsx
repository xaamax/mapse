import { DotsVerticalIcon } from "@radix-ui/react-icons";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Edit2 } from "lucide-react";
import { Link } from "react-router-dom";
import { ProjetoSocialRegistroDTO } from "@/core/dto/projeto-social-dto";

type Props = {
  row: ProjetoSocialRegistroDTO;
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
        <Link to={`/projetos-sociais/${row?.id}`}>
          <DropdownMenuItem>
            Editar
            <DropdownMenuShortcut>
              <Edit2 className="h-4 w-4" />
            </DropdownMenuShortcut>
          </DropdownMenuItem>
        </Link>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
