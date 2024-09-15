import { PageContainer, ProCard } from "@ant-design/pro-components";

import { BlogEditForm } from '@/components/Admin/Blog/EditDetail/blog-edit-form';
import { createFileRoute } from '@tanstack/react-router'
import { message } from "antd";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute('/admin/blog/edit/$id')({
  component:BlogEditDetailRoute
})

export function BlogEditDetailRoute() {
  // const [form] = Form.useForm();

  const { id } = useParams({ strict: false });
  const { data, isLoading } = { data: [], isLoading: false}
  const [updateBlog, other] = [(args) => args, { isLoading: false }]
  return (
    <PageContainer>
      <ProCard loading={isLoading}>
        <BlogEditForm
          loading={other.isLoading}
          data={data || {}}
          onFinish={async (v: any) => {
            const values = v;
            if (id) values.id = Number(id);
            const data = {
              type: "",
              data: {
                ...values,
              },
            };
            const result: any = await updateBlog(data);

            if (result.data && result.data.code === 1) {
              message.error(result.data.message);
              return false;
            } else {
              message.success(result.data.message);
              return true;
            }
          }}
        />
      </ProCard>
    </PageContainer>
  );
}
