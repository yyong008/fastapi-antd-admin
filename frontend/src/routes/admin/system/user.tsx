import "@/components/Admin/System/User/styles.css";

import { useEffect, useState } from "react";

import { PageContainer } from "@ant-design/pro-components";
import { UserProTable } from "@/components/Admin/System/User/user-pro-table";
import { createFileRoute } from "@tanstack/react-router";
import { getUsers } from "@/apis/user";

export function UserRoute() {
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
    const res: any = await getUsers({ ...page });

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
      <UserProTable
        {...{
          data: data ?? [],
          isLoading: false,
          refetch: () => {},
          depts: [],
          roles: [],
          page: 1,
          setPage: () => {},
        }}
      />
    </PageContainer>
  );
}

export const Route = createFileRoute("/admin/system/user")({
  component: UserRoute,
});
