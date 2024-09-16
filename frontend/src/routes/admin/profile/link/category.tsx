import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";
import { useEffect, useState } from "react";

import { DeleteIt } from "@/components/Admin/Profile/Link/delete-it";
import { Link } from "@tanstack/react-router";
import { LinkCategoryModalCreate } from "@/components/Admin/Profile/Link/link-category-modal-create";
import { LinkCategoryModalUpdate } from "@/components/Admin/Profile/Link/link-category-modal-update";
import { createFileRoute } from '@tanstack/react-router'
import { getProfileLinkCategory } from "@/apis/admin/profile/link/category";

export const Route = createFileRoute('/admin/profile/link/category')({
  component: LinkCategoryRoute
})

export function LinkCategoryRoute() {
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {

    const res: any = await getProfileLinkCategory({ ...page });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page]);
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        headerTitle="链接分类管理"
        search={false}
        loading={loading}
        options={{
          reload: getData,
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
                    refetch={getData}
                  />
                  <DeleteIt record={record} refetch={getData} title="删除" />
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
