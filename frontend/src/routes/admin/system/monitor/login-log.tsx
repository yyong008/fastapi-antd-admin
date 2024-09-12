import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { createColumns } from "@/components/Admin/System/Monitor/LoginLog/create-columns";
import { createFileRoute } from "@tanstack/react-router";
import { getMonitorLoginLog } from "@/apis/admin/system/minitor.login-log";

export const Route = createFileRoute("/admin/system/monitor/login-log")({
  component: LoginLogComponent,
});

function LoginLogComponent() {
  const [ loading, setLoading ] = useState(false)
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    total: 0,
    list: [],
  });
  const getData = async () => {
    const res: any = await getMonitorLoginLog({
      page: page.page,
      pageSize: page.pageSize,
    })

    if(res && res?.code === 0 ) {
      setData(res.data)
      setLoading(false)
    }
  }

  useEffect(() => {
    getData();
    setLoading(true)
  }, [page])

  return (
    <PageContainer>
      <ProTable
        size="small"
        search={false}
        headerTitle="登录记录"
        rowKey="id"
        showSorterTooltip
        dataSource={data?.list || []}
        columns={createColumns()}
        loading={loading}
        options={{
          // reload: refetch,
        }}
        pagination={{
          total: data?.total || 0,
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
