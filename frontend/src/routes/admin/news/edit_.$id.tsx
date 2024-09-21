import { Button, Space, message } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { NewsEditDrawer } from "@/components/Admin/News/Edit/NewsEdit";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsById } from "@/apis/admin/news/news";
import { updateNewsCategoryById } from "@/apis/admin/news/category";
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

  const getData = async () => {
    const res: any = await getNewsById(Number(id));
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
  return (
    <PageContainer>
      <ProCard
        loading={loading}
        style={{ height: 600 }}
        title="修改新闻"
        tooltip=""
        extra={
          <Space>
            <NewsEditDrawer
              trigger={<Button type="primary">修改新闻</Button>}
              onFinish={async (v) => {
                const result: any = await updateNewsCategoryById(id, v);
                if (result && result?.code !== 0) {
                  message.error(result?.message);
                  return false;
                }
                message.success(result?.message);
                // nav({
                //   to: `/admin/news/result`,
                //   state: {
                //     // title: v.title, id: result.data.data.id
                //   },
                // });
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
