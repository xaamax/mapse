import { Checkbox } from "@/components/ui/checkbox";
import { DataTableColumnHeader } from "@/components/data-table/data-table-column-header";
import { DataTableRowActions } from "./row-actions";
import { ProjetoSocialRegistroDTO } from "@/core/dto/projeto-social-dto";
import { ColumnDef, Row } from "@tanstack/react-table";

export const columns = (
  _?: (index: number) => void,
  toogleRefreshTable?: () => void,
): ColumnDef<ProjetoSocialRegistroDTO>[] => [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected()
            ? true
            : table.getIsSomePageRowsSelected()
              ? "indeterminate"
              : false
        }
        onCheckedChange={(value) =>
          table.toggleAllPageRowsSelected(Boolean(value))
        }
        aria-label="Selecionar todos"
        className="translate-y-[2px]"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(Boolean(value))}
        aria-label="Selecionar linha"
        className="translate-y-[2px]"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },

  {
    accessorKey: "nome",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Nome" />
    ),
    meta: { title: "Nome" },
    cell: ({ row }) => <div>{row.getValue("nome")}</div>,
    filterFn: (row: Row<ProjetoSocialRegistroDTO>, id, value: string[]) =>
      value.includes(row.getValue(id)),
  },
  {
    accessorKey: "categoria_nome",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Categoria" />
    ),
    meta: { title: "Categoria" },
    cell: ({ row }) => <div>{row.getValue("categoria_nome")}</div>,
    filterFn: (row: Row<ProjetoSocialRegistroDTO>, id, value: string[]) =>
      value.includes(row.getValue(id)),
  },
  {
    accessorKey: "publico_alvo_nome",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Público alvo" />
    ),
    meta: { title: "Público alvo" },
    cell: ({ row }) => <div>{row.getValue("publico_alvo_nome")}</div>,
    filterFn: (row: Row<ProjetoSocialRegistroDTO>, id, value: string[]) =>
      value.includes(row.getValue(id)),
  },
  {
    id: "actions",
    cell: ({ row }) => (
      <DataTableRowActions
        row={row.original}
        {...{ toogleRefreshTable }}
      />
    ),
  },
];
