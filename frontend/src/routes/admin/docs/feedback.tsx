import { PageContainer, ProTable } from "@ant-design/pro-components";

import { FeedbackModalCreate } from "@/components/Admin/Docs/Feedback/FeedbackModalCreate";
import { FormatTime } from "@/components/common/format-time";
import { Image } from "antd";
import { createFileRoute } from '@tanstack/react-router'
import { useState } from "react";

export const Route = createFileRoute('/admin/docs/feedback')({
  component: FeedbackRoute
})

export function FeedbackRoute() {
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const { data, isLoading, refetch } =  {
    data: {
      list: [],
      total: 0
    },
    isLoading: false,
    refetch: v => v
  }

  const columns = [
    {
      dataIndex: "id",
      title: "反馈编号",
    },
    {
      dataIndex: "content",
      title: "反馈内容",
    },
    {
      dataIndex: "url",
      title: "反馈图片",
      render(_: any, record: any) {
        return (
          <div className="w-[100px]">
            <Image src={record.url}></Image>
          </div>
        );
      },
    },
    {
      dataIndex: "createdAt",
      title: "反馈时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.createdAt} />;
      },
    },
  ];
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="反馈内容"
        size="small"
        search={false}
        loading={isLoading}
        dataSource={data?.list ?? []}
        columns={columns}
        options={{
          reload: refetch,
        }}
        toolBarRender={() => [
          <FeedbackModalCreate
            key="changelog-modal-create"
            refetch={refetch}
          />,
        ]}
        pagination={{
          total: data?.total || 0,
          pageSize: page.pageSize || 10,
          onChange(page, pageSize) {
            setPage({ page, pageSize });
          },
        }}
      />
    </PageContainer>
  );
}