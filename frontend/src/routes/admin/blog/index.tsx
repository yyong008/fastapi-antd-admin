import { PageContainer, ProTable } from "@ant-design/pro-components";

// import { blogColumnsCreate } from "@/components/Admin/Blog/Index/blog-columns-create";
// import { createBlogCategoryToolBarRender } from "@/components/Admin/Blog/Index/blog-tool-bar-render";
import { createFileRoute } from '@tanstack/react-router'
// import { useEffect, useMemo } from "react";
// import { useParams, useSearch } from "@tanstack/react-router";

// import { message } from "antd";

export const Route = createFileRoute('/admin/blog/')({
  component: BlogIndexRoute
})

export function BlogIndexRoute() {
  // const [searchParams] = useSearch({ strict: false });
  // const { data, isLoading } = useReadBlogListQuery({
  //   page: 1,
  //   pageSize: 10,
  //   tag: searchParams.get("tag"),
  //   category: searchParams.get("category"),
  // });
  // const { dataSource, tag: tagInfo, category: categoryInfo } = data?.data || {};

  // const fetcher = () => {}

  // const info = useMemo(() => {
  //   let name = "";
  //   if (searchParams.get("category") && categoryInfo?.name)
  //     name = "分类: " + categoryInfo?.name;
  //   if (searchParams.get("tag") && tagInfo?.name)
  //     name = "标签: " + tagInfo?.name;

  //   return { name, categoryName: categoryInfo?.name, tagName: tagInfo?.name };
  // }, [categoryInfo?.name, searchParams, tagInfo?.name]);

  // useEffect(() => {
  //   if (data?.code === 1) {
  //     message.error(data?.message);
  //   }
  // }, [data]);

  return (
    <PageContainer>
      <ProTable
        loading={false}
        rowKey="id"
        size="small"
        search={false}
        dataSource={[]}
        // headerTitle={info.name}
        // toolBarRender={() => createBlogCategoryToolBarRender(lang!)}
        // columns={blogColumnsCreate(lang!, fetcher, info) as any}
      />
    </PageContainer>
  );
}
