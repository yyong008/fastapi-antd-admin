import { PageContainer, ProCard } from "@ant-design/pro-components";

import { LoginIn } from "@/components/Admin/Dashboard/login-in";
import { SignIn } from "@/components/Admin/Dashboard/sign-in";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/dashboard/")({
  component: DashboardRoute,
});

export function DashboardRoute() {
  const userInfo = {};
  const _data = { data: {}, isLoading: false };
  const { data, isLoading } = _data || {};

  return (
    <PageContainer loading={isLoading}>
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
