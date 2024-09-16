import { Link, useParams } from "@tanstack/react-router";
import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { ButtonLink } from "@/components/common/button-link";
import { DeleteIt } from "@/components/common/delete-it";
import { Space } from "antd";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsListByCategoryId } from "@/apis/admin/news/news";

export const Route = createFileRoute("/admin/news/category/$id")({
  component: NewsRoute,
});

export function NewsRoute() {
  const { id: category_id } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {
    const res: any = await getNewsListByCategoryId({ ...page, category_id });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="新闻"
        size="small"
        search={false}
        loading={loading}
        options={{
          reload: getData,
        }}
        dataSource={data?.list}
        toolBarRender={() => [
          <ButtonLink
            key="create-news-modal"
            type="new"
            content="添加新闻"
            to={`/admin/news/edit`}
          />,
        ]}
        columns={[
          {
            dataIndex: "title",
            title: "新闻标题",
            renderText(_, record: any) {
              return <Link to={`/news/${record.id}`}>{record.title}</Link>;
            },
          },
          {
            dataIndex: "content",
            title: "新闻内容",
            render(_, record) {
              return <div>{record.content?.slice(0, 20)}</div>;
            },
          },
          {
            dataIndex: "author",
            title: "作者",
          },
          {
            dataIndex: "source",
            title: "新闻来源",
          },
          {
            dataIndex: "newsId",
            title: "新闻分类",
          },
          {
            dataIndex: "viewCount",
            title: "查看次数",
          },
          {
            dataIndex: "op",
            title: "操作",
            render(_, record) {
              return (
                <Space>
                  <ButtonLink
                    type="edit"
                    to={`/admin/news/edit/${record.id}`}
                  />
                  <DeleteIt
                    refetch={getData as any}
                    record={record}
                    title={""}
                  />
                </Space>
              );
            },
          },
        ]}
      />
    </PageContainer>
  );
}

