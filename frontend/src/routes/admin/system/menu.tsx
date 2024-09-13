import { useEffect, useState } from "react";

import { MenuProTable } from "@/components/Admin/System/Menu/menu-pro-table";
import { PageContainer } from "@ant-design/pro-components";
import { createFileRoute } from "@tanstack/react-router";
import { getAllMenuTree } from "@/apis/admin/system/menu";

export const Route = createFileRoute("/admin/system/menu")({
  component: MenuRoute,
});

function MenuRoute() {
  const [loading, setLoading] = useState(false);
  const [menu, setMenu] = useState([]);

  const getData = async () => {
    setLoading(true);
    const menuRes: any = await getAllMenuTree();

    if (menuRes && menuRes.code === 0) {
      setMenu(menuRes?.data);
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
        menuNotPerm={[]}
        reload={() => {}}
      />
    </PageContainer>
  );
}
