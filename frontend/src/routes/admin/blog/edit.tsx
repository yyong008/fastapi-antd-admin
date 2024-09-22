import { PageContainer, ProCard } from "@ant-design/pro-components";

import { BlogCreateForm } from "@/components/Admin/Blog/EditNew/blog-create-form";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/blog/edit")({
  component: EditBlogRoute,
});

export function EditBlogRoute() {
  return (
    <PageContainer>
      <ProCard>
        <BlogCreateForm />
      </ProCard>
    </PageContainer>
  );
}
