import * as ic from "@ant-design/icons";

import { Button, message } from "antd";

import BlogCategoryModalForm from "./blog-category-modal-form";
import { updateBlogCategoryById } from "@/apis/admin/blog/category";
import { useParams } from "@tanstack/react-router";
import { useState } from "react";

const { EditOutlined } = ic;

export default function BlogCategoryModalUpdate({ record, refetch }: any) {
  const { id } = record.id;
  const [loading, setLoading] = useState(false);
  return (
    <BlogCategoryModalForm
      loding={loading}
      title="修改分类"
      onOpenChange={(_: any, form: any) => {
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={<Button type={"link"} icon={<EditOutlined />} />}
      onFinish={async (values: any, form: any) => {
        setLoading(true);
        const data = {
          ...values,
        };
        data.categoryId = record.id
        const result: any = await updateBlogCategoryById(record.id, data);
        setLoading(false);
        if (result.code === 0) {
          message.success(result.message);
          refetch();
          form.resetFields();
          return false;
        }
        message.error(result.message);
        setLoading(false);

        return true;
      }}
    />
  );
}
