import { Button } from "antd";
import { EditOutlined } from "@ant-design/icons";
import { NewsCategoryModalBase } from "./NewCategoryModalBase";
import { createNewsCategory } from '@/apis/admin/news/category'
import { useState } from "react";

export function NewsCategoryModalCreate({ refetch }: any) {
  const [loading, setLoading] = useState(false)
  return (
    <NewsCategoryModalBase
      refetch={refetch}
      loading={loading}
      key={Date.now()}
      title="创建新建分类"
      trigger={
        <Button type={"primary"} icon={<EditOutlined />}>
          新建新闻分类
        </Button>
      }
      onOpenChange={() => {}}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        setLoading(true)

        const result: any = await createNewsCategory(values);
        setLoading(false)
        return result
      }}
    >
    </NewsCategoryModalBase>
  );
}
