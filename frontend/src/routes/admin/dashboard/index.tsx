import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { LoginIn } from "@/components/Admin/Dashboard/login-in";
import { SignIn } from "@/components/Admin/Dashboard/sign-in";
import { createFileRoute } from "@tanstack/react-router";
import { getDashboardData } from "@/apis/admin/dashboard";

export const Route = createFileRoute("/admin/dashboard/")({
  component: DashboardRoute,
});

// getDashboardData
export function DashboardRoute() {
  const userInfo = JSON.parse(localStorage.getItem("userInfo") || "{}");
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

    const res: any = await getDashboardData();

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page]);

  return (
    <PageContainer loading={loading}>
      <ProCard>
        <ProCard>
          <div className="flex justify-between">
            <LoginIn data={data} userInfo={userInfo} />
            <SignIn data={data} />
          </div>
        </ProCard>
      </ProCard>
    </PageContainer>
  );
}
