import { PageContainer, ProCard } from "@ant-design/pro-components";

import { ConfigProTable } from '@/components/Admin/System/Config/config-pro-table';
import { createFileRoute } from '@tanstack/react-router'

export function ConfigRoute() {
  return (
    <PageContainer>
      <ProCard>
        <ConfigProTable />
      </ProCard>
    </PageContainer>
  );
}


export const Route = createFileRoute('/admin/system/config')({
  component: ConfigRoute
})
