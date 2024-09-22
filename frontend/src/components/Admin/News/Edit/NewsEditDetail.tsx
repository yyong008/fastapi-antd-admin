import { DrawerForm, ProForm } from "@ant-design/pro-components";

import { NewsEditItem } from "./NewsEditItem";
import { message } from "antd";
import { updateNews } from "@/apis/admin/news/news";
import { useEffect } from "react";
import { useNavigate } from "@tanstack/react-router";

type NewsEditDetailDrawerProps = {
  trigger: any;
  id: number;
  data: any;
  newsCategory: any;
  content: string;
};

export function NewsEditDetailDrawer(props: NewsEditDetailDrawerProps) {
  const nav = useNavigate();
  const [form] = ProForm.useForm();
  useEffect(() => {
    form.setFieldsValue(props.data);
    form.setFieldValue("content", props.content);
  }, [props.data, props.content]);

  return (
    <DrawerForm
      form={form}
      title="修改新闻"
      trigger={props.trigger}
      onFinish={async (values) => {
        const result: any = await updateNews(props.id, values);
        if (result?.code !== 0) {
          message.error(result?.message);
          return false;
        }
        message.success(result?.message);
        nav({
          to: `/admin/news/result`,
          state: {
            title: values.title,
            id: result.data.id,
            type: "update",
          } as any,
        });
        return true;
      }}
    >
      <NewsEditItem
        newsCategory={props.newsCategory || []}
        content={props.content}
      />
    </DrawerForm>
  );
}
