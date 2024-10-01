import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useMemo, useState } from "react";

import { ButtonLink } from "@/components/common/button-link";
import { createFileRoute } from "@tanstack/react-router";
import { createMaiListColumns } from "@/components/Admin/Tools/MailList/mail-list-columns-create";
import { getToolsMail } from "@/apis/admin/tools/mail"

export const Route = createFileRoute("/admin/tools/mail/list")({
  component: MailListRoute,
});

export function MailListRoute() {
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
    const res: any = await getToolsMail({ ...page });
    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);
  const columns = useMemo(() => {
    return createMaiListColumns({ refetch: getData });
  }, []);

  return (
    <PageContainer>
      <ProTable
        loading={loading}
        size="small"
        search={false}
        headerTitle="邮件模板"
        rowKey="id"
        showSorterTooltip
        dataSource={data?.list || []}
        toolBarRender={() => [
          <ButtonLink
            key="create-mail"
            to={`/admin/tools/mail`}
            type={"new"}
            content="去新建"
          />,
        ]}
        columns={columns as any}
        options={{
          reload: getData,
        }}
        pagination={{
          total: data?.total,
          pageSize: 10,
          current: page.page,
          onChange(page, pageSize) {
            setPage({
              page,
              pageSize,
            });
          },
        }}
      />
    </PageContainer>
  );
}
