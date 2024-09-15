import { PageContainer, ProTable } from "@ant-design/pro-components";
import { createFileRoute, useSearch } from '@tanstack/react-router'
import { useEffect, useState } from "react";

import { blogColumnsCreate } from "@/components/Admin/Blog/Index/blog-columns-create";
import { createBlogCategoryToolBarRender } from "@/components/Admin/Blog/Index/blog-tool-bar-render";
import { getBlog } from "@/apis/admin/blog/blog";

// import { useEffect, useMemo } from "react";
// import { useParams, useSearch } from "@tanstack/react-router";

// import { message } from "antd";

export const Route = createFileRoute('/admin/blog/')({
  component: BlogIndexRoute
})

export function BlogIndexRoute() {
  const search = useSearch({ strict: false });
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
    const ids: any = {}
    if(search.category) {
      ids.categoryId = search.category
    }

    if(search.tag) {
      ids.tagId = search.tag
    }
    const res: any = await getBlog({ ...page, ...ids });
    if (res && res.code === 0) {
      setData(res.data);

    }

    setLoading(false);
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);
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
        loading={loading}
        rowKey="id"
        size="small"
        search={false}
        dataSource={data.list || []}
        // headerTitle={info.name}
        toolBarRender={() => createBlogCategoryToolBarRender()}
        columns={blogColumnsCreate({}) as any}
      />
    </PageContainer>
  );
}
