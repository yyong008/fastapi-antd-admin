import { PageContainer, ProTable } from "@ant-design/pro-components";

import { DictModalCreate } from "@/components/Admin/System/Dict/dict/create-dict-modal";
import { createColumns } from "@/components/Admin/System/Dict/dict-pro-table/create-columns";
import { createFileRoute } from "@tanstack/react-router";
import { getDict } from "@/apis/admin/system/dict";
import { useGetPageData } from "@/hooks/useGetPageData";

export const Route = createFileRoute("/admin/system/dict")({
  component: DictRoute,
});

export function DictRoute() {
  const { loading, data, getData } = useGetPageData({
    request: getDict,
  });
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        search={false}
        headerTitle="字典项目"
        loading={loading}
        toolBarRender={() => [
          <DictModalCreate refetch={getData} key="create-dict-modal" />,
        ]}
        dataSource={data.list ?? []}
        columns={createColumns({ refetch: getData })}
        options={{
          reload: getData,
        }}
      />
    </PageContainer>
  );
}
