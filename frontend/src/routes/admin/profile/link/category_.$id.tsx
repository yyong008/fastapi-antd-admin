import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { LinkModalCreate } from "@/components/Admin/Profile/LinkCategoryDetail/link-modal-create";
import { createFileRoute } from "@tanstack/react-router";
import { createLinkCategoryDetailColumns } from "@/components/Admin/Profile/LinkCategoryDetail/createLinkCategoryDetailColumns";
import { getProfileLinkListByCategoryId } from "@/apis/admin/profile/link/link";
import { useParams } from "@tanstack/react-router";

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
    const res: any = await getProfileLinkListByCategoryId(id, { ...page });

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
        columns={createLinkCategoryDetailColumns({ refetch: getData })}
      />
    </PageContainer>
  );
}
