import * as ic from "@ant-design/icons";

import { Button, message } from "antd";

import { BlogTagModalForm } from "./blog-tag-modal-form";
import { useParams } from "@tanstack/react-router";

const { EditOutlined } = ic;

export function BlogTagModalUpdate({ record, refetch }: any) {
  const { id } = useParams({ strict: false });
  const [updateBlogTag] = [(...args: any) => args]
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

        data.categoryId = Number(id);
        data.id = record.id;
        const result = await updateBlogTag(data);
        if (result.data.code !== 0) {
          message.error(result.data.message);
          return false;
        }
        message.success(result.data.message);
        form.resetFields();
        refetch();
        return true;
      }}
    />
  );
}
