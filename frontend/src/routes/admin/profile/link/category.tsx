import { Link, useParams } from "@tanstack/react-router";
import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";

import { DeleteIt } from "@/components/Admin/Profile/Link/delete-it";
import { LinkCategoryModalCreate } from "@/components/Admin/Profile/Link/link-category-modal-create";
import { LinkCategoryModalUpdate } from "@/components/Admin/Profile/Link/link-category-modal-update";
import { createFileRoute } from '@tanstack/react-router'
import { useState } from "react";

export const Route = createFileRoute('/admin/profile/link/category')({
  component: LinkCategoryRoute
})

export function LinkCategoryRoute() {
  const { id } = useParams({ strict: false });
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
    category: id,
  });
  const { data, isLoading, refetch } = { data: { list: [], total: 0 }, isLoading: false, refetch: () => { } };
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        headerTitle="链接分类管理"
        search={false}
        loading={isLoading}
        options={{
          reload: refetch,
        }}
        toolBarRender={() => [
          <LinkCategoryModalCreate key="link-category-modal-create" />,
        ]}
        dataSource={data?.list || []}
        columns={[
          {
            dataIndex: "name",
            title: "链接分类名",
            render(_, record) {
              return <LinkTag record={record} />;
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
                  <LinkCategoryModalUpdate
                    key="link-category-modal-modify"
                    record={record}
                    refetch={refetch}
                  />
                  <DeleteIt record={record} refetch={refetch} title="删除" />
                </Space>
              );
            },
          },
        ]}
        pagination={{
          total: data?.total,
          pageSize: 10,
          onChange(_page, pageSize) {
            setPage({
              ...page,
              page: _page,
              pageSize,
            });
          },
        }}
      />
    </PageContainer>
  );
}

function LinkTag({ record }: any) {
  return (
    <Link to={`/admin/profile/link/category/${record?.id}`}>
      <Tag color="blue">{record?.name}</Tag>
    </Link>
  );
}
