import { DrawerForm, ProForm } from "@ant-design/pro-components";

import { NewsEditItem } from "./NewsEditItem";
import { createNews } from "@/apis/admin/news/news";
import { message } from "antd";
import { useEffect } from "react";
import { useNavigate } from "@tanstack/react-router";

type NewsEditDrawerProps = {
  trigger: any;
  newsCategory: any[];
  content: string;
};

export function NewsEditDrawer(props: NewsEditDrawerProps) {
  const nav = useNavigate();

  const [form] = ProForm.useForm();
  useEffect(() => {
    form.setFieldsValue(props.content);
  }, [props.content]);

  return (
    <DrawerForm
      title="创建新闻"
      trigger={props.trigger}
      onFinish={async (values) => {
        const result: any = await createNews(values);
        if (result?.code !== 0) {
          message.error(result?.message);
          return false;
        }
        message.success(result?.message);
        nav({
          to: `/admin/news/result`,
          state: {
            title: values.title,
            id: result.data.id
          } as any,
        });
        return true;
      }}
      onFinishFailed={(value) => {
        message.error(value.toString());
      }}
    >
      <NewsEditItem
        newsCategory={props.newsCategory || []}
        content={props.content}
      />
    </DrawerForm>
  );
}
