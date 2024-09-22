import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { createFileRoute } from "@tanstack/react-router";
import { createNewsCategoryColumns } from "@/components/Admin/News/CategoryDetailList/createColumns";
import { createToolBarRender } from "@/components/Admin/News/CategoryDetailList/createToolBarRender";
import { getNewsListByCategoryId } from "@/apis/admin/news/news";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/news/category/$id")({
  component: NewsRoute,
});

export function NewsRoute() {
  const { id: category_id } = useParams({ strict: false });
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
    const res: any = await getNewsListByCategoryId({ ...page, category_id });

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
        headerTitle="新闻"
        size="small"
        search={false}
        loading={loading}
        options={{
          reload: getData,
        }}
        dataSource={data?.list}
        toolBarRender={createToolBarRender()}
        columns={createNewsCategoryColumns({ refetch: getData })}
      />
    </PageContainer>
  );
}
