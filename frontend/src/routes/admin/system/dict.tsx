import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { DictModal } from "@/components/Admin/System/Dict/dict/create-dict-modal";
import { createColumns } from "@/components/Admin/System/Dict/dict-pro-table/create-columns";
import { createFileRoute } from '@tanstack/react-router'
import { getDict } from "@/apis/admin/system/dict";

export const Route = createFileRoute('/admin/system/dict')({
  component :DictRoute
})

export function DictRoute() {
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {

    const res: any = await getDict({ ...page });

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
        rowKey="id"
        size="small"
        search={false}
        headerTitle="字典项目"
        loading={loading}
        toolBarRender={() => [
          <DictModal record={{}} key="create-dict-modal" />,
        ]}
        dataSource={ data.list ?? []}
        columns={createColumns()}
        options={{
          // reload: refetch,
        }}
      />
    </PageContainer>
  );
}
