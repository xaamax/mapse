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

  const { data } = useGetAllProjetosSociais({
    page_number: 1,
    page_size: paginationState.pageSize,
  });


  
  return (
    <div className="w-full space-y-4">
      <PageTitle title="Projetos Sociais" desc="Gerencie os registros de projetos sociais" />

      <DataTable
        data={data?.data?.items || []}
        columns={columns()}
        pathInclude="/projetos-sociais/incluir"
        facetedFilters={[
          { field: 'nome', label: 'Nome' },
          { field: 'endereco', label: 'Endereço' },
          { field: 'situacao', label: 'Situação' },
        ]}
      />
    </div>
  );
}
