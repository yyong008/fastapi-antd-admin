import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "@tanstack/react-router";

import { Button } from "antd";
import { DictItemModalCreate } from "@/components/Admin/System/DictItem/create-dict-item-modal";
import { createColumns } from "@/components/Admin/System/DictItem/dict-item-pro-table/create-columns";
import { createFileRoute } from "@tanstack/react-router";
import { getDictItem } from "@/apis/admin/system/dict-item";

// import { useGetPageData } from "@/hooks/useGetPageData"

export const Route = createFileRoute("/admin/system/dict-item/$id")({
  component: DictItemRoute,
});

export function DictItemRoute() {
  const router = useRouter();
  const { id } = useParams({ strict: false });
  // const { loading, getData, setData, page, setPage } = useGetPageData({ request: getDictItem })
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
    const res: any = await getDictItem(Number(id), { ...page });

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
    <PageContainer loading={loading}>
      <ProTable
        rowKey="id"
        size="small"
        search={false}
        headerTitle="字典项目"
        loading={loading}
        options={
          {
            reload: getData,
          }
        }
        toolBarRender={() => [
          <DictItemModalCreate dictId={id} key="create-dict-modal" refetch={getData}/>,
          <Button
            key="2"
            onClick={() => {
              router.history.go(-1);
            }}
          >
            返回
          </Button>,
        ]}
        dataSource={data?.list || []}
        columns={createColumns({ refetch: getData, dictId: 1 })}
        pagination={{
          total: data?.total,
          pageSize: page.pageSize || 10,
          // onChange(_page, pageSize) {
          //   // setPage({ ...page, page: _page, pageSize });
          // },
        }}
      />
    </PageContainer>
  );
}


