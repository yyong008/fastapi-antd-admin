import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { NewsEditDrawer } from "@/components/Admin/News/Edit/NewsEdit";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsCategory } from "@/apis/admin/news/category";

export const Route = createFileRoute("/admin/news/edit")({
  component: NewsEditRoute,
});

export function NewsEditRoute() {
  const [loading, setLoading] = useState(false);
  const [content, setContent] = useState("");
  const [newsCategoryData, setNewsCategoryData] = useState([]);

  const getData = async () => {
    setLoading(true);
    const newsCategoryRes: any = await getNewsCategory({
      page: 1,
      pageSize: 10000,
    });

    if (newsCategoryRes && newsCategoryRes.code === 0) {
      setNewsCategoryData(newsCategoryRes.data.list);
    }
    setLoading(false);
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, []);
  return (
    <PageContainer loading={loading}>
      <ProCard
        title="编辑新闻（创建）"
        extra={
          <Space>
            <NewsEditDrawer
              newsCategory={newsCategoryData}
              content={content}
              trigger={<Button type="primary">创建新闻</Button>}
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
