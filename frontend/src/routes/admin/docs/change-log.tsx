import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { ChangeLogCreateModal } from "@/components/Admin/Docs/ChangeLog/ChangeLogModalCreate";
import { createChangeLogColumns } from "@/components/Admin/Docs/ChangeLog/ChangeLogColumns";
import { createFileRoute } from "@tanstack/react-router";
import { getDocsChangelog } from "@/apis/admin/docs/changelog";
import { useSearch } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/docs/change-log")({
  component: ChangeLogRoute,
});

export function ChangeLogRoute() {
  const params = useSearch({ strict: false });
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
    const res: any = await getDocsChangelog({ ...page });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="更新日志"
        size="small"
        search={false}
        dataSource={data?.list ?? []}
        loading={loading}
        columns={createChangeLogColumns({ refresh: getData })}
        toolBarRender={() => [
          <ChangeLogCreateModal
            key="changelog-modal-create"
            refetch={getData}
          />,
        ]}
        options={{
          reload: getData,
        }}
        pagination={{
          total: data.total,
          pageSize: Number(params.pageSize ?? 10),
          onChange(page, pageSize) {
            setPage({ page, pageSize });
          },
        }}
      />
    </PageContainer>
  );
}
