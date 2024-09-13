import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { CreateDeptModal } from "@/components/Admin/System/Dept/create-dept-modal";
import { createColumns } from "@/components/Admin/System/Dept/dept-pro-table/create-columns";
import { createFileRoute } from '@tanstack/react-router'
import { getDepts } from "@/apis/admin/system/dept";

export const Route = createFileRoute('/admin/system/dept')({
  component: DeptRoute
})

export function DeptRoute() {
  const [page] = useState({
    page: 1,
    pageSize: 1000,
  });
  const [data, setData] = useState({
    list: [],
    total: 0
  })

  const getData = async () => {
    const res:any = await getDepts({ ...page })
    if(res && res.code ===0) {
      setData(res.data)
    }

  }


  useEffect(() => {
    getData()
  }, [])
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        headerTitle="部门管理"
        search={false}
        pagination={false}
        // loading={isLoading}
        options={{
          // reload: refetch,
        }}
        toolBarRender={() => [<CreateDeptModal record={{}} key="dept-modal" />]}
        dataSource={data?.list || []}
        columns={createColumns()}
      />
    </PageContainer>
  );
}
