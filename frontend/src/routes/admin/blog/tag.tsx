import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { blogTagColumnsCreate } from "@/components/Admin/Blog/Tag/blog-tag-columns-create";
import { blogTagToolBarRender } from "@/components/Admin/Blog/Tag/blog-tag-tool-bar-render";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogTag } from "@/apis/admin/blog/tag";

export const Route = createFileRoute("/admin/blog/tag")({
  component: BlogTagRoute,
});

export function BlogTagRoute() {
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
    const res: any = await getBlogTag({ ...page });
    if (res && res.code === 0) {
      setData(res.data);
    }

    setLoading(false);
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
        search={false}
        loading={loading}
        dataSource={data?.list ?? []}
        toolBarRender={() => blogTagToolBarRender(getData)}
        columns={blogTagColumnsCreate(getData)}
        options={{
          reload: getData,
        }}
        pagination={{
          total: data?.total ?? 0,
          pageSize: 10,
          onChange(page, pageSize) {
            setPage?.(() => ({ page, pageSize }));
          },
        }}
      />
    </PageContainer>
  );
}
