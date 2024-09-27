import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { BlogEditForm } from "@/components/Admin/Blog/EditDetail/blog-edit-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogById } from "@/apis/admin/blog/category";
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
  const [data, setData] = useState({});

  const getData = async () => {
    const res: any = await getBlogById(Number(id));
    if (res && res.code === 0) {
      setLoading(false);
      setData(res.data);
      setContent(res.data.content);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page, id]);
  return <PageContainer>
      <ProCard
        title="编辑博客（创建）"
        extra={
          <Space>
            <BlogEditForm
              data={data}
              loading={loading}
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
}
