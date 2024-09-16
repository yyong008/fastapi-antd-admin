import { PageContainer, ProConfigProvider } from "@ant-design/pro-components";

import { ProjectAbout } from "@/components/Client/About/project-about";
import { ProjectDevelopmentDep } from "@/components/Client/About/production-development-dep";
import { ProjectInfo } from "@/components/Client/About/project-info";
import { ProjectProductionDep } from "@/components/Client/About/project-production-dep";
import { Space } from "antd";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/about/")({
  component: AdminAboutComponent,
});

export function AdminAboutComponent() {
  return (
    <PageContainer>
      <ProConfigProvider>
        <Space direction="vertical">
          <ProjectAbout />
          <ProjectInfo />
          <ProjectProductionDep />
          <ProjectDevelopmentDep />
        </Space>
      </ProConfigProvider>
    </PageContainer>
  );
}
