import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { StorageModal } from "@/components/Admin/Tools/Storage/storage-modal";
import { createFileRoute } from '@tanstack/react-router'
import { getToolsStorage } from "@/apis/admin/tools/storage";
import { storageColumnsCreate } from "@/components/Admin/Tools/Storage/storage-columns-create";

export const Route = createFileRoute('/admin/tools/storage')({
  component: ToolsStorageRoute
})

export function ToolsStorageRoute() {
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {

    const res: any = await getToolsStorage({ ...page });
    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page]);
  return (
    <PageContainer>
      <ProTable
        loading={loading}
        size="small"
        search={false}
        headerTitle="文件上传"
        rowKey="id"
        showSorterTooltip
        dataSource={data?.list || []}
        toolBarRender={() => [<StorageModal key="storage" refetch={getData} />]}
        columns={storageColumnsCreate() as any}
        options={{
          reload: getData,
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
