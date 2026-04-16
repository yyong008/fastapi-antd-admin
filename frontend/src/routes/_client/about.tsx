import { ProConfigProvider } from "@ant-design/pro-components";
import { ProjectAbout } from "@/components/Client/About/project-about";
import { ProjectDevelopmentDep } from "@/components/Client/About/production-development-dep";
import { ProjectInfo } from "@/components/Client/About/project-info";
import { ProjectProductionDep } from "@/components/Client/About/project-production-dep";
import { Space } from "antd";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_client/about")({
  component: AboutComponent,
});

export function AboutComponent() {
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-slate-900">About</h1>
        <p className="mt-2 text-sm text-slate-500">Project overview and dependency details.</p>
      </div>
      <ProConfigProvider>
        <Space className="w-full" direction="vertical" size="middle">
          <ProjectAbout />
          <ProjectInfo />
          <ProjectProductionDep />
          <ProjectDevelopmentDep />
        </Space>
      </ProConfigProvider>
    </section>
  );
}
