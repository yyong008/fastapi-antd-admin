import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";

import { BlogCreateForm } from "@/components/Admin/Blog/EditNew/blog-create-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/admin/blog/edit")({
  component: EditBlogRoute,
});

export function EditBlogRoute() {
  const [content, setContent] = useState("");
  return (
    <PageContainer>
      <ProCard
        title="编辑博客（创建）"
        extra={
          <Space>
            <BlogCreateForm
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
