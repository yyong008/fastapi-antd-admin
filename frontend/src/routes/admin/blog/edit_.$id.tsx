import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { BlogEditForm } from "@/components/Admin/Blog/EditDetail/blog-edit-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogById } from "@/apis/admin/blog/category";
import { getBlogCategory } from "@/apis/admin/blog/category";
import { getBlogTag } from "@/apis/admin/blog/tag";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/blog/edit/$id")({
  component: BlogEditDetailRoute,
});

export function BlogEditDetailRoute() {
  const [content, setContent] = useState("");
  const { id } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    categories: [],
    tags: [],
  });

  const getData = async () => {
    const page = {
      page: 1,
      pageSize: 1000,
    };
    const resBT: any = await getBlogCategory(page);
    const resBC: any = await getBlogTag(page);
    const res: any = await getBlogById(Number(id));
    if (res && res.code === 0) {
      setLoading(false);
      setData((p) => ({
        ...p,
        ...res.data,
      }));
      setContent(res.data.content);
    }

    if (resBT && resBT.code === 0) {
      setData((p) => ({
        ...p,
        categories: resBT.data.list || [],
      }));
    }

    if (resBC && resBC.code === 0) {
      setData((p) => ({
        ...p,
        tags: resBC.data.list || [],
      }));
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page, id]);
  return (
    <PageContainer loading={loading}>
      <ProCard
        title="编辑博客（创建）"
        extra={
          <Space>
            <BlogEditForm
              id={id}
              categories={data.categories}
              tags={data.tags}
              data={data}
              content={content}
              trigger={<Button type="primary">编辑博客</Button>}
            />
          </Space>
        }
      >
        <div>
          <QuillEditor content={content} setContent={setContent} />
        </div>
      </ProCard>
    </PageContainer>
  );
}
