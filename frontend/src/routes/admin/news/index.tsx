import { PageContainer, ProTable } from "@ant-design/pro-components";

import { ButtonLink } from '@/components/common/button-link';
import { DeleteIt } from '@/components/common/delete-it';
import { Link } from "@tanstack/react-router";
import { Space } from "antd";
import { createFileRoute } from '@tanstack/react-router'
import { useState } from "react";

export const Route = createFileRoute('/admin/news/')({
  component: () => <div>Hello /admin/news/list!</div>
})

export function NewsRoute() {
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const { data, isLoading, refetch } = {
    data: {
      list: [],
      total: 0,
    },
    isLoading: true,
    refetch: (...args: any[]) => {},
  }
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="新闻"
        size="small"
        search={false}
        loading={isLoading}
        options={{
          reload: refetch,
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
              return (
                <Link to={`/news/${record.id}`}>{record.title}</Link>
              );
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
                  <DeleteIt refetch={refetch as any} record={record} title={""} />
                </Space>
              );
            },
          },
        ]}
      />
    </PageContainer>
  );
}
