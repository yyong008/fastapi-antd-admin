import { DrawerForm, ProForm } from "@ant-design/pro-components";

import { NewsEditItem } from "./NewsEditItem";
import { useEffect } from "react";

type NewsEditDetailDrawerProps = {
  trigger: any;
  onFinish: any;
  data: any;
  newsCategory: any;
}

export function NewsEditDetailDrawer(props: NewsEditDetailDrawerProps) {
  const [form] = ProForm.useForm()
  useEffect(() => {
    form.setFieldsValue(props.data)
  }, [props.data])

  return (
    <DrawerForm
      form={form}
      title="修改新闻"
      trigger={props.trigger}
      onFinish={async (values) => {
        props.onFinish(values);
      }}
    >
      <NewsEditItem newsCategory={props.newsCategory || []} />
    </DrawerForm>
  );
}
