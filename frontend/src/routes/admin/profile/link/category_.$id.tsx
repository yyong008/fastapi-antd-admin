import { Link, useParams } from "@tanstack/react-router";
import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";
import { useEffect, useState } from "react";

import { LinkModalCreate } from "@/components/Admin/Profile/LinkCategoryDetail/link-modal-create";
import { LinkModalUpdate } from "@/components/Admin/Profile/LinkCategoryDetail/link-modal-update";
import LinkSvg from "@/components/Admin/Profile/LinkCategoryDetail/link-svg";
import { createFileRoute } from "@tanstack/react-router";
import { getProfileLinkListByCategoryId } from "@/apis/admin/profile/link/link";

export const Route = createFileRoute("/admin/profile/link/category/$id")({
  component: LinkCategoryDetailRoute,
});

export function LinkCategoryDetailRoute() {
  const { id } = useParams({ strict: false });
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

    const res: any = await getProfileLinkListByCategoryId(id,{ ...page });

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
        search={false}
        loading={loading}
        dataSource={data?.list || []}
        toolBarRender={() => [
          <LinkModalCreate refetch={getData} key="create-link-modal" />,
        ]}
        options={{
          reload: getData,
        }}
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
        columns={[
          {
            dataIndex: "name",
            title: "链接名",
          },
          {
            dataIndex: "url",
            title: "链接地址",
            renderText(_, record: any) {
              return (
                <Link to={record.url} target="_blank">
                  <Tag className="inline-flex" color="cyan">
                    {record.url}
                    <LinkSvg className="border-yellow-200 w-[16px]" />
                  </Tag>
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
                  <LinkModalUpdate
                    refetch={getData}
                    record={record}
                    key="modify-link-modal"
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
