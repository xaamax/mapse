import { Checkbox } from "@/components/ui/checkbox";
import { DataTableColumnHeader } from "@/components/data-table/data-table-column-header";
import { ProjetoSocialEscolarRegistroDTO } from "@/core/dto/projeto-social-escolar-dto";
import { ColumnDef, Row } from "@tanstack/react-table";
import { DataTableRowActions } from "./row-actions";

export const columns = (
  _?: (index: number) => void,
  toogleRefreshTable?: () => void,
): ColumnDef<ProjetoSocialEscolarRegistroDTO>[] => [
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
    accessorKey: "ue_nome",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Unidade Educacional" />
    ),
    meta: { title: "UE" },
    cell: ({ row }) => <div>{row.getValue("ue_nome")}</div>,
    filterFn: (
      row: Row<ProjetoSocialEscolarRegistroDTO>,
      id,
      value: string[],
    ) => value.includes(row.getValue(id)),
  },

  {
    accessorKey: "dre_nome",
    header: ({ column }) => (
      <DataTableColumnHeader
        column={column}
        title="Diretoria Regional de Educação"
      />
    ),
    meta: { title: "DRE" },
    cell: ({ row }) => <div>{row.getValue("dre_nome")}</div>,
    filterFn: (
      row: Row<ProjetoSocialEscolarRegistroDTO>,
      id,
      value: string[],
    ) => value.includes(row.getValue(id)),
  },
  {
    id: "actions",
    cell: ({ row }) => (
      <DataTableRowActions row={row.original} {...{ toogleRefreshTable }} />
    ),
  },
];
