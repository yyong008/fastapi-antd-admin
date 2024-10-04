import { getAllMenuTree, getAllMenuTreeNoPermission } from "@/apis/admin/system/menu";
import { useEffect, useState } from "react";

import { MenuProTable } from "@/components/Admin/System/Menu/menu-pro-table";
import { PageContainer } from "@ant-design/pro-components";
import { ResponseStatus } from "@/constants/status";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/system/menu")({
  component: MenuRoute,
});

function MenuRoute() {
  const [loading, setLoading] = useState(false);
  const [menu, setMenu] = useState([]);
  const [menuNotPerm, setMenuNotPerm] = useState([])
  const getData = async () => {
    setLoading(true);
    const menuRes: any = await getAllMenuTree();
    const menuNotPermRes: any = await getAllMenuTreeNoPermission()

    if (menuRes && menuRes.code === ResponseStatus.S) {
      setMenu(menuRes?.data);
      setLoading(false);
    }

    if (menuNotPermRes && menuNotPermRes.code === ResponseStatus.S) {
      setMenuNotPerm(menuNotPermRes?.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    getData();
  }, []);
  return (
    <PageContainer loading={loading}>
      <MenuProTable
        menuRaw={menu}
        loading={false}
        menuNotPerm={menuNotPerm ?? []}
        refetch={getData}
      />
    </PageContainer>
  );
}
