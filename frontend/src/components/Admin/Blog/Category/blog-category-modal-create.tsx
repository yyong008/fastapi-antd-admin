import * as ic from "@ant-design/icons";

import { Button, message } from "antd";

import BlogCategoryModalForm from "./blog-category-modal-form";
import { createBlogCategory } from "@/apis/admin/blog/category";
import { useState } from "react";

const { EditOutlined } = ic;

export function BlogCategoryModalCreate({ refetch }: any) {
  const [loading, setLoading] = useState(false);
  return (
    <BlogCategoryModalForm
      loading={loading}
      title="创建分类"
      trigger={
        <Button type="primary" icon={<EditOutlined />}>
          新建
        </Button>
      }
      onOpenChange={() => {}}
      onFinish={async (values: any, form: any) => {
        setLoading(true);
        const data = {
          ...values,
        };
        const result: any = await createBlogCategory(data);
        setLoading(false);
        if (result && result.code === 0) {
          message.success(result?.message || "创建成功");
          refetch?.();
          form.resetFields();
          return false;
        }
        message.error(result?.message || "创建失败");

        return true;
      }}
    />
  );
}
