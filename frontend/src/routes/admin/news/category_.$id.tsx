import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useMemo, useState } from "react";

import { createFileRoute } from "@tanstack/react-router";
import { createNewsCategoryColumns } from "@/components/Admin/News/CategoryDetailList/createColumns";
import { createToolBarRender } from "@/components/Admin/News/CategoryDetailList/createToolBarRender";
import { getNewsCategory } from "@/apis/admin/news/category";
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

  const [newsCategoryData, setNewsCategoryData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {
    const res: any = await getNewsListByCategoryId({ ...page, category_id });
    const newsRes: any = await getNewsCategory({ page: 1, pageSize: 10000 });
    setLoading(false);
    if (res && res.code === 0) {
      setData(res.data);
    }

    if (newsRes && newsRes.code === 0) {
      setNewsCategoryData(newsRes.data);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);

  const name = useMemo(() => {
    const nc = newsCategoryData?.list?.filter(
      (item: any) => item.id === Number(category_id)
    )[0] as any;
    return nc?.name || "";
  }, [newsCategoryData]);
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle={
          <div className="flex items-center gap-2">
            <div className="text-xl font-bold">{name}</div>新闻
          </div>
        }
        size="small"
        search={false}
        loading={loading}
        options={{
          reload: getData,
        }}
        dataSource={data?.list}
        toolBarRender={createToolBarRender()}
        columns={createNewsCategoryColumns({
          refetch: getData,
          newsCategoryData,
        })}
      />
    </PageContainer>
  );
}
