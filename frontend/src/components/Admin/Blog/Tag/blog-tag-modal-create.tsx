import { Button, message } from "antd";

import { BlogTagModalForm } from "./blog-tag-modal-form";
import { EditOutlined } from "@ant-design/icons";
import { createBlogTag } from "@/apis/admin/blog/tag";

export function BlogTagModalCreate({ refetch }: any) {
  return (
    <BlogTagModalForm
      title="创建标签"
      trigger={
        <Button type={"primary"} icon={<EditOutlined />}>
          新建
        </Button>
      }
      onOpenChange={() => {}}
      onFinish={async (values: any, form: any) => {
        const result: any = await createBlogTag(values);
        if (result && result.code === 0) {
          message.success(result.message);
          form.resetFields();
          refetch();
          return true;
        }
        message.error(result.message);
        return false;
      }}
    />
  );
}
