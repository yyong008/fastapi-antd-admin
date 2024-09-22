import { DrawerForm } from "@ant-design/pro-components";
import { Form } from "antd";
import { NewsEditItem } from "./NewsEditItem";
import { useEffect } from "react";

type NewsEditDetailDrawerProps = {
  trigger: any;
  onFinish: any;
  data: any;
  newsCategory: any;
}

export function NewsEditDetailDrawer(props: NewsEditDetailDrawerProps) {
  const [form] = Form.useForm()
  useEffect(() => {
    // console.log(props.data)
    form.setFieldsValue(props.data)
  }, [props.data])

  console.log(props)
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
