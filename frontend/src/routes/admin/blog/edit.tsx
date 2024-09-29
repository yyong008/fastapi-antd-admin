import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { BlogCreateForm } from "@/components/Admin/Blog/EditNew/blog-create-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogCategory } from "@/apis/admin/blog/category";
import { getBlogTag } from "@/apis/admin/blog/tag";

export const Route = createFileRoute("/admin/blog/edit")({
  component: EditBlogRoute,
});

export function EditBlogRoute() {
  const [content, setContent] = useState("");
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
    getData();
  }, []);
  return (
    <PageContainer>
      <ProCard
        title="编辑博客（创建）"
        extra={
          <Space>
            <BlogCreateForm
              categories={data.categories}
              tags={data.tags}
              content={content}
              trigger={<Button type="primary">创建博客</Button>}
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
