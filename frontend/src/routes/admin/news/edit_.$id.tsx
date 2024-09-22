import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { NewsEditDetailDrawer } from "@/components/Admin/News/Edit/NewsEditDetail";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsById } from "@/apis/admin/news/news";
import { getNewsCategory } from "@/apis/admin/news/category";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/news/edit/$id")({
  component: EditDetailRoute,
});

export function EditDetailRoute() {
  const { id } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);
  const [content, setContent] = useState("");
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({});
  const [newsCategoryData, setNewsCategoryData] = useState([]);

  const getData = async () => {
    const res: any = await getNewsById(Number(id));
    const newsCategoryRes: any = await getNewsCategory({
      page: 1,
      pageSize: 10000,
    });
    if (res && res.code === 0) {
      setLoading(false);
      setData(res.data);
      setContent(res.data.content);
    }

    if (newsCategoryRes && newsCategoryRes.code === 0) {
      setNewsCategoryData(newsCategoryRes.data.list);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page, id]);
  return (
    <PageContainer>
      <ProCard
        loading={loading}
        style={{ height: 600 }}
        title="修改新闻"
        tooltip=""
        extra={
          <Space>
            <NewsEditDetailDrawer
              id={id}
              data={data}
              content={content}
              newsCategory={newsCategoryData}
              trigger={<Button type="primary">修改新闻</Button>}
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
