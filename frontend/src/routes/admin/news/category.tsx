import { Link, Outlet } from "@tanstack/react-router";
import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";

import { DeleteIt } from "@/components/common/delete-it";
import { NewsCategoryModalCreate } from "@/components/Admin/News/Category/news-category-modal-create";
import { NewsCategoryModalUpdate } from "@/components/Admin/News/Category/news-category-modal-update";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/admin/news/category")({
  component: NewsCategoryRoute,
});

export function NewsCategoryRoute() {
  const [setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const { data, isLoading, refetch } = {
    data: {
      total: 0,
      list: [],
    },
    isLoading: false,
    refetch: () => {},
  };

  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        headerTitle="新闻分类"
        search={false}
        loading={isLoading}
        options={{
          reload: refetch,
        }}
        pagination={{
          total: data?.total,
          pageSize: 10,
          // onChange(page, pageSize) {
          //   // setPage({
          //   //   page,
          //   //   pageSize,
          //   // });
          // },
        }}
        toolBarRender={() => [
          <NewsCategoryModalCreate
            key="news-category-modal-create"
            refetch={refetch}
          />,
        ]}
        dataSource={data?.list}
        columns={[
          {
            dataIndex: "name",
            title: "新闻分类名",
            render(_, record: any) {
              return (
                <Link to={`/admin/news/category/${record.id}`}>
                  <Tag color="blue">{record.name}</Tag>
                </Link>
              );
            },
          },
          {
            dataIndex: "description",
            title: "描述",
          },
          {
            dataIndex: "op",
            title: "操作",
            render(_, record) {
              return (
                <Space>
                  <NewsCategoryModalUpdate
                    key="news-category-modal-modify"
                    record={record}
                    refetch={refetch}
                  />
                  <DeleteIt record={record} refetch={refetch} title="删除" />
                </Space>
              );
            },
          },
        ]}
      />
      <Outlet />
    </PageContainer>
  );
}
