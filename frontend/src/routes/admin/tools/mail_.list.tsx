import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useMemo, useState } from "react";

import { ButtonLink } from "@/components/common/button-link";
import { createFileRoute } from "@tanstack/react-router";
import { createMaiListColumns } from "@/components/Admin/Tools/MailList/mail-list-columns-create";

export const Route = createFileRoute("/admin/tools/mail/list")({
  component: MailListRoute,
});

export function MailListRoute() {
  const { lang } = { lang: "en-US" };
  const [page, setPage] = useState({
    page: 1,
    pageSize: 110,
  });
  const { data, isLoading, refetch } = {
    data: {
      list: [],
      total: 0,
    },
    isLoading: false,
    refetch: (args) => args,
  };

  const columns = useMemo(() => {
    return createMaiListColumns(lang!);
  }, [lang]);

  return (
    <PageContainer>
      <ProTable
        loading={isLoading}
        size="small"
        search={false}
        headerTitle="登录记录"
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
          reload: refetch,
        }}
        pagination={{
          total: data?.total,
          pageSize: 10,
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
