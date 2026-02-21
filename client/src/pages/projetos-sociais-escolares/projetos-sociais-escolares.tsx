import { useState } from "react";
import { columns } from "./components/columns";
import PageTitle from "@/components/commons/page-title";
import { PaginationState } from "@tanstack/react-table";
import { useGetAllProjetosSociaisEscolares } from "@/core/apis/queries/projeto-social-escolar";
import { DataTable } from "@/components/data-table/data-table";

export function ProjetosSociaisEscolares() {
  const [paginationState, setPaginationState] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  });

  const { data, isLoading } = useGetAllProjetosSociaisEscolares({
    page_number:
      paginationState.pageIndex === 0
        ? 1
        : paginationState.pageIndex * paginationState.pageSize,
    page_size: paginationState.pageSize,
  });

  return (
    <div className="w-full space-y-4">
      <PageTitle
        title="Projetos Sociais Escolares"
        desc="Gerencie os registros de projetos sociais nas escolas"
      />

      <DataTable
        data={data?.data?.items || []}
        columns={columns()}
        pathInclude="/projetos-sociais-escolares/incluir"
        facetedFilters={[
          { field: "dre_nome", label: "DRE" },
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
