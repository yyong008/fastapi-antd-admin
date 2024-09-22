import * as ic from "@ant-design/icons";

import { Button, message } from "antd";

import BlogCategoryModalForm from "./blog-category-modal-form";
import { useParams } from "@tanstack/react-router";

const { EditOutlined } = ic;

export default function BlogCategoryModalUpdate({ record, refetch }: any) {
  const { id } = useParams({ strict: false });
  const [updateBlogCategory, other] = [
    (...args: any) => args,
    { isLoading: false },
  ];

  return (
    <BlogCategoryModalForm
      loding={other.isLoading}
      title="修改分类"
      onOpenChange={(_: any, form: any) => {
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={<Button type={"link"} icon={<EditOutlined />} />}
      onFinish={async (values: any, form: any) => {
        const data = {
          ...values,
        };
        data.categoryId = Number(id);
        data.id = record.id;
        const result: any = await updateBlogCategory(data);
        if (result.data.code === 1) {
          message.error(result.data.message);
          return false;
        }
        message.success(result.data.message);
        refetch();
        form.resetFields();
        return true;
      }}
    />
  );
}
