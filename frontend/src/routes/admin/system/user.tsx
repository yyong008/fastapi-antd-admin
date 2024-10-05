import "@/components/Admin/System/User/styles.css";

import { useEffect, useState } from "react";

import { PageContainer } from "@ant-design/pro-components";
import { UserProTable } from "@/components/Admin/System/User/user-pro-table";
import { createFileRoute } from "@tanstack/react-router";
import { getAllRoles } from "@/apis/admin/system/role";
import { getDeptsListAll } from "@/apis/admin/system/dept";
import { getUsers } from "@/apis/admin/system/user";

export function UserRoute() {
  const [loading, setLoading] = useState(false);
  const [depts, setDepts] = useState([])
  const [roles, setRoles] = useState([])
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getDeptData = async () => {
    const res: any = await getDeptsListAll();
    if (res && res.code === 0) {
      setDepts(res.data.list);
    }
  }
  const getRoleData = async () => {
    const res: any = await getAllRoles();
    if (res && res.code === 0) {
      setRoles(res.data.list);
    }
  }
  const getData = async () => {
    const res: any = await getUsers({ ...page });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
    getDeptData()
    getRoleData()
  }, [page]);
  return (
    <PageContainer>
      <UserProTable
        {...{
          data: data ?? [],
          isLoading: loading,
          refetch: getData,
          depts,
          roles,
          page: page.page || 1,
          setPage: setPage,
        }}
      />
    </PageContainer>
  );
}

export const Route = createFileRoute("/admin/system/user")({
  component: UserRoute,
});
