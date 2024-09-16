import { Link, Outlet } from "@tanstack/react-router";
import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";
import { useEffect, useState } from "react";

import { DeleteIt } from "@/components/common/delete-it";
import { NewsCategoryModalCreate } from "@/components/Admin/News/Category/news-category-modal-create";
import { NewsCategoryModalUpdate } from "@/components/Admin/News/Category/news-category-modal-update";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsCategory } from "@/apis/admin/news/category";

export const Route = createFileRoute("/admin/news/category")({
  component: NewsCategoryRoute,
});

export function NewsCategoryRoute() {
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

    const res: any = await getNewsCategory({ ...page });

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
        headerTitle="新闻分类"
        search={false}
        loading={loading}
        options={{
          reload: getData,
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
            refetch={getData}
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
                    refetch={getData}
                  />
                  <DeleteIt record={record} refetch={getData as any} title="删除" />
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
