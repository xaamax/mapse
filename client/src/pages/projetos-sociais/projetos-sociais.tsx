import { useState } from "react";
import { columns } from "./components/columns";
import PageTitle from "@/components/commons/page-title";
import { PaginationState } from "@tanstack/react-table";
import { useGetAllProjetosSociais } from "@/core/apis/queries/projeto-social";
import { DataTable } from "@/components/data-table/data-table";

export function ProjetosSociais() {
  const [paginationState, setPaginationState] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  });

  const { data, isLoading } = useGetAllProjetosSociais({
    page_number: paginationState.pageIndex === 0 ? 1 : paginationState.pageIndex * paginationState.pageSize,
    page_size: paginationState.pageSize,
  });

  return (
    <div className="w-full space-y-4">
      <PageTitle
        title="Projetos Sociais"
        desc="Gerencie os registros de projetos sociais"
      />

      <DataTable
        data={data?.data?.items || []}
        columns={columns()}
        pathInclude="/projetos-sociais/incluir"
        facetedFilters={[
          { field: "nome", label: "Nome" },
          { field: "categoria_nome", label: "Categoria" },
          { field: "publico_alvo_nome", label: "Público alvo" },
        ]}
        loading={isLoading}
        rowCount={data?.data?.total_items}
        manualPagination={true}
        paginationState={paginationState}
        onPaginationChange={setPaginationState}
      />
    </div>
  );
}
