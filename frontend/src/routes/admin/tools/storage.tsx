import { PageContainer, ProTable } from "@ant-design/pro-components";

import { StorageModal } from "@/components/Admin/Tools/Storage/storage-modal";
import { createFileRoute } from '@tanstack/react-router'
import { storageColumnsCreate } from "@/components/Admin/Tools/Storage/storage-columns-create";
import { useState } from "react";

export const Route = createFileRoute('/admin/tools/storage')({
  component: ToolsStorageRoute
})

export function ToolsStorageRoute() {
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const { data, isLoading, refetch } = { data: { list: [], total: 0}, isLoading: false, refetch: () => {}}
  return (
    <PageContainer>
      <ProTable
        loading={isLoading}
        size="small"
        search={false}
        headerTitle="文件上传"
        rowKey="id"
        showSorterTooltip
        dataSource={data?.list || []}
        toolBarRender={() => [<StorageModal key="storage" refetch={refetch} />]}
        columns={storageColumnsCreate() as any}
        options={{
          reload: refetch,
        }}
        pagination={{
          total: data?.total,
          pageSize: 10,
          onChange(_page, pageSize) {
            setPage({
              ...page,
              page: _page,
              pageSize,
            });
          },
        }}
      />
    </PageContainer>
  );
}
