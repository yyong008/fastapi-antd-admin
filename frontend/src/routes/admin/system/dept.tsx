import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { CreateDeptModal } from "@/components/Admin/System/Dept/create-dept-modal";
import { createColumns } from "@/components/Admin/System/Dept/dept-pro-table/create-columns";
import { createFileRoute } from "@tanstack/react-router";
import { getDepts } from "@/apis/admin/system/dept";

export const Route = createFileRoute("/admin/system/dept")({
  component: DeptRoute,
});

export function DeptRoute() {
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 1000,
  });
  const [options, setOptions] = useState([]);
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {
    setLoading(true);
    const res: any = await getDepts({ ...page });
    setLoading(false);
    if (res && res.code === 0) {
      setData(res.data);
      setOptions(res.data.list.map((item: any) => ({
        label: item.name,
        value: item.id,
      })));
    }
  };

  useEffect(() => {
    getData();
  }, []);
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        size="small"
        headerTitle="部门管理"
        search={false}
        pagination={false}
        loading={loading}
        options={
          {
            reload: getData,
          }
        }
        toolBarRender={() => [<CreateDeptModal options={options}  refetch={getData} key="dept-modal" />]}
        dataSource={data?.list || []}
        columns={createColumns({ refetch: getData, options: options })}
      />
    </PageContainer>
  );
}
