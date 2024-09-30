import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { LinkCategoryModalCreate } from "@/components/Admin/Profile/Link/link-category-modal-create";
import { createFileRoute } from "@tanstack/react-router";
import { createProfileLinkCategories } from "@/components/Admin/Profile/Link/createProfileCategoryColumns";
import { getProfileLinkCategory } from "@/apis/admin/profile/link/category";

export const Route = createFileRoute("/admin/profile/link/category")({
  component: LinkCategoryRoute,
});

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
    setLoading(true);
    getData();
  }, [page]);
  return (
    <PageContainer loading={loading}>
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
          <LinkCategoryModalCreate refetch={getData} key="link-category-modal-create" />,
        ]}
        dataSource={data?.list || []}
        columns={createProfileLinkCategories({  refetch: getData })}
        pagination={{
          total: data?.total,
          current: page.page,
          pageSize: 10,
          onChange(_page, pageSize) {
            setPage((p) => ({
              ...p,
              page: _page,
              pageSize,
            }));
          },
        }}
      />
    </PageContainer>
  );
}
