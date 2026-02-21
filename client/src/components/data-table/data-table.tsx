/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState } from "react";
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFacetedRowModel,
  getFacetedUniqueValues,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { DataTablePagination } from "@/components/data-table/data-table-pagination";
import { DataTableToolbar } from "@/components/data-table/data-table-toolbar";
import DataTableLoader from "./data-table-loader";

interface DataTableProps<TData> {
  columns: ColumnDef<TData>[];
  data: TData[];
  facetedFilters?: { field: string; label: string }[];
  pathInclude?: string;
  manualPagination?: boolean;
  paginationState?: {
    pageIndex: number;
    pageSize: number;
  };
  onPaginationChange?: React.Dispatch<
    React.SetStateAction<{ pageIndex: number; pageSize: number }>
  >;
  rowCount?: number;
  loading?: boolean;
}

export function DataTable<TData>({
  columns,
  data,
  facetedFilters,
  pathInclude,
  manualPagination,
  paginationState,
  onPaginationChange,
  rowCount,
  loading = false,
}: DataTableProps<TData>) {
  const [rowSelection, setRowSelection] = useState({});
  const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({});
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
  const [sorting, setSorting] = useState<SortingState>([]);
  const [globalFilter, setGlobalFilter] = React.useState("");
  const globalFilterFn = React.useCallback(
    (row: any, _columnId: string, filterValue: string) => {
      const searchValue = filterValue.toLowerCase();

      const getValue = (obj: any): any => {
        if (Array.isArray(obj)) {
          return obj.flatMap((item) => getValue(item));
        }
        if (typeof obj === "object" && obj !== null) {
          return Object.values(obj).flatMap((value) => getValue(value));
        }
        return [String(obj).toLowerCase()];
      };

      const flattenedValues = getValue(row.original);
      return flattenedValues.some((value: any) => value.includes(searchValue));
    },
    [],
  );

  const table = useReactTable({
    data,
    columns,
    state: {
      sorting,
      columnVisibility,
      rowSelection,
      columnFilters,
      globalFilter,
      pagination: paginationState,
    },
    enableRowSelection: true,
    onRowSelectionChange: setRowSelection,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    onColumnVisibilityChange: setColumnVisibility,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFacetedRowModel: getFacetedRowModel(),
    getFacetedUniqueValues: getFacetedUniqueValues(),
    onGlobalFilterChange: setGlobalFilter,
    globalFilterFn,
    manualPagination: manualPagination,
    rowCount: rowCount,
    onPaginationChange: onPaginationChange,
  });

  return (
    <div className="space-y-4">
      {loading ? (
        <DataTableLoader
          table={table}
          rowCount={paginationState?.pageSize as number}
        />
      ) : (
        <>
          <DataTableToolbar
            table={table}
            facetedFilters={facetedFilters}
            pathInclude={pathInclude}
          />
          <div className="rounded-md border">
            <Table>
              <TableHeader>
                {table.getHeaderGroups().map((headerGroup) => (
                  <TableRow key={headerGroup.id} className="group/row">
                    {headerGroup.headers.map((header) => {
                      return (
                        <TableHead
                          key={header.id}
                          colSpan={header.colSpan}
                          className={
                            header.column.columnDef.meta?.className ?? ""
                          }
                        >
                          {header.isPlaceholder
                            ? null
                            : flexRender(
                                header.column.columnDef.header,
                                header.getContext(),
                              )}
                        </TableHead>
                      );
                    })}
                  </TableRow>
                ))}
              </TableHeader>
              <TableBody>
                {table.getRowModel().rows?.length ? (
                  table.getRowModel().rows.map((row) => (
                    <TableRow
                      key={row.id}
                      data-state={row.getIsSelected() && "selected"}
                      className="group/row"
                    >
                      {row.getVisibleCells().map((cell) => (
                        <TableCell
                          key={cell.id}
                          className={
                            cell.column.columnDef.meta?.className ?? ""
                          }
                        >
                          {flexRender(
                            cell.column.columnDef.cell,
                            cell.getContext(),
                          )}
                        </TableCell>
                      ))}
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell
                      colSpan={columns.length}
                      className="h-24 text-center"
                    >
                      Nenhum registro encontrado.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </div>
        </>
      )}
      {manualPagination && <DataTablePagination table={table} />}
    </div>
  );
}
