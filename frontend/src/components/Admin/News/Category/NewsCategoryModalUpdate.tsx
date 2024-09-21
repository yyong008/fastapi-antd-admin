import { Button } from "antd";
import { EditOutlined }from "@ant-design/icons";
import { NewsCategoryModalBase } from "./NewCategoryModalBase";
import { updateNewsCategoryById } from "@/apis/admin/news/category";
import { useAntdThemeToken } from "@/hooks/use-antd-theme-token";
import { useState } from "react";

export function NewsCategoryModalUpdate({ record, refetch }: any) {
  const token = useAntdThemeToken();
  const iconStyles = { style: { color: token.colorPrimary } };
  const [loading, setLoading] = useState(false)
  return (
    <NewsCategoryModalBase
      refetch={refetch}
      loading={loading}
      key={Date.now()}
      title={"修改新闻分类"}
      onOpenChange={(c, form) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={
        <Button
          type={"link"}
          icon={<EditOutlined {...iconStyles} />}
        />
      }
      onFinish={async (values: any) => {
        setLoading(true)
        const result: any = await updateNewsCategoryById(record.id, values);
        setLoading(false)
        return result
      }}
    >
    </NewsCategoryModalBase>
  );
}
