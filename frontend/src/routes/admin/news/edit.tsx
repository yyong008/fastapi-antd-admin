import { Button, Space, message } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";

import { NewsEditDrawer } from "@/components/Admin/News/Edit/NewsEdit";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { useNavigate } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/admin/news/edit")({
  component: NewsEditRoute,
});

export function NewsEditRoute() {
  const nav = useNavigate();
  const [content, setContent] = useState("");
  const [createNews] = [(args) => args];
  return (
    <PageContainer>
      <ProCard
        style={{ height: 600 }}
        title="新闻"
        tooltip=""
        extra={
          <Space>
            <NewsEditDrawer
              trigger={<Button type="primary">添加新闻</Button>}
              onFinish={async (v) => {
                const result = await createNews(v);
                if (result.data?.code !== 0) {
                  message.error(result.data?.message);
                  return false;
                }
                message.success(result.data?.message);
                nav({
                  to: `/admin/news/result`,
                  state: {
                    // title: v.title, id: result.data.data.id
                  },
                });
                return true;
              }}
            />
          </Space>
        }
      >
        <div style={{ height: "400px" }}>
          <QuillEditor content={content} setContent={setContent} />
        </div>
      </ProCard>
    </PageContainer>
  );
}
