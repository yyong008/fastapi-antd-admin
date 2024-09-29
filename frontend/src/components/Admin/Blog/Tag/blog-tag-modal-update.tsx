import { Button, message } from "antd";

import { BlogTagModalForm } from "./blog-tag-modal-form";
import { EditOutlined } from "@ant-design/icons";
import { updateBlogTagById } from "@/apis/admin/blog/tag";

export function BlogTagModalUpdate({ record, refetch }: any) {
  return (
    <BlogTagModalForm
      title="修改标签"
      onOpenChange={(c: any, form: any) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={<Button type="link" icon={<EditOutlined />}></Button>}
      onFinish={async (values: any, form: any) => {
        const data = values;

        data.categoryId = record.id

        const result: any = await updateBlogTagById(record.id, data);
        if (result && result.code === 0) {
          message.success(result.message);
          form.resetFields()
          refetch();
          return true;
        }
        message.error(result.message);
        return false;
      }}
    />
  );
}
