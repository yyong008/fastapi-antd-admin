import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useMemo, useRef, useState } from "react";

import { CreateRoleModal } from "@/components/Admin/System/Role/create-role-modal/index.tsx";
import { createColumns } from "@/components/Admin/System/Role/role-pro-table/create-columns.tsx";
import { createFileRoute } from "@tanstack/react-router";
import { genMenuTreeForRole } from "@/utils/genMenuTreeForRole";
import { getAllMenuList } from "@/apis/admin/system/menu";
import { getAllRoles } from "@/apis/admin/system/role";

export const Route = createFileRoute("/admin/system/role")({
  component: RoleRoute,
});

export function RoleRoute() {
  const [loading, setLoading] = useState(false);
  const actionRef = useRef();

  const [data, setData] = useState({
    list: [],
    total: 0,
  });
  const [menu, setMenu] = useState([]);

  const getData = async () => {
    setLoading(true);
    const res: any = await getAllRoles();
    const menuRes: any = await getAllMenuList();
    setLoading(false);
    if (res && res.code === 0) {
      setData(res.data);
    }
    if (menuRes && menuRes.code === 0) {
      setMenu(menuRes?.data);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  const menus = useMemo(() => {
    if (menu) {
      return genMenuTreeForRole(menu || [], null);
    }
  }, [menu]);

  return (
    <PageContainer>
      <ProTable
        size="small"
        actionRef={actionRef}
        rowKey="id"
        search={false}
        loading={loading}
        dataSource={data?.list || []}
        columns={createColumns({ menus, refetch: getData }) as any}
        options={
          {
            reload: getData,
          }
        }
        toolBarRender={() => [
          <CreateRoleModal
            key="create-role-modal"
            menu={menus as any}
            refetch={getData}
          />,
        ]}
      />
    </PageContainer>
  );
}
