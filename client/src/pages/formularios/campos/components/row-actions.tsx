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
import { CampoDetalhesDTO } from "@/core/dto/campo-dto";

type Props = {
  row: CampoDetalhesDTO;
  onClickEdit?: (row: CampoDetalhesDTO) => void;
};

export function RowActions({ row, onClickEdit }: Props) {

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="ghost"
          size="icon"
          className="flex h-8 w-8 p-0 data-[state=open]:bg-muted text-primary"
        >
          <DotsVerticalIcon className="h-4 w-4" />
          <span className="sr-only">Abrir menu</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-[160px]">
          <DropdownMenuItem onClick={() => onClickEdit?.(row)}>
            Editar
            <DropdownMenuShortcut>
              <Edit2 className="h-4 w-4" />
            </DropdownMenuShortcut>
          </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
