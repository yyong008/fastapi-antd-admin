import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { createFileRoute } from "@tanstack/react-router";
import { createNewsCategoryColumns } from "@/components/Admin/News/Category/createNewsCategoryColumns";
import { createToolBarRender } from "@/components/Admin/News/Category/createToolBarRender";
import { getNewsCategory } from "@/apis/admin/news/category";

export const Route = createFileRoute("/admin/news/category")({
  component: NewsCategoryRoute,
});

export function NewsCategoryRoute() {
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
    const res: any = await getNewsCategory({ ...page });

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
        size="small"
        headerTitle="新闻分类"
        search={false}
        loading={loading}
        options={{
          reload: getData,
        }}
        dataSource={data?.list}
        columns={createNewsCategoryColumns({ refetch: getData })}
        toolBarRender={createToolBarRender({ refetch: getData })}
        pagination={{
          total: data?.total,
          pageSize: page.pageSize,
          onChange(page, pageSize) {
            setPage({
              page,
              pageSize,
            });
          },
        }}
      />
    </PageContainer>
  );
}
