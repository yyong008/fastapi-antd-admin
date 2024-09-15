import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { blogCategoryColumnsCreate } from "@/components/Admin/Blog/Category/blog-category-columns-create";
import { createBlogCategoryToolBarRender } from "@/components/Admin/Blog/Category/blog-category-tool-bar-render";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogCategory } from "@/apis/admin/blog/category";

export const Route = createFileRoute("/admin/blog/category")({
  component: BlogCategoryRoute,
});

export function BlogCategoryRoute() {
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
    const res: any = await getBlogCategory({ ...page });
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
        dataSource={data?.list || ([] as any[])}
        toolBarRender={() => createBlogCategoryToolBarRender(() => {})}
        columns={blogCategoryColumnsCreate("en-US", () => {})}
        options={
          {
            // reload: refetch,
          }
        }
        pagination={{
          total: data?.total,
          pageSize: 10,
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
