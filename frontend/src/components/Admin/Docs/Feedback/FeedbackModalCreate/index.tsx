import { Button, Form, message } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { FeedbackItems } from "../FeedbackItems";
import { ModalForm } from "@ant-design/pro-components";
import { createDocsFeedback } from "@/apis/admin/docs/feedback";
import { useState } from "react";

export function FeedbackModalCreate({ refetch }: any) {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title="创建反馈"
      loading={loading}
      onOpenChange={() => {}}
      trigger={
        <Button type="primary" icon={<EditOutlined />}>
          新建
        </Button>
      }
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={2000}
      onFinish={async (values: any) => {

        const data = { ...values };
        if (values.file && values.file.length > 0) {
          const url: string = values.file[0].response.data.url;
          data.url = url
        }

        delete data.file;
        setLoading(true);
        const result: any = await createDocsFeedback(data);
        setLoading(false);
        if (result && result?.code === 0) {
          message.success(result?.message);
          refetch();
          form.resetFields();
          return true;
        }
        message.error(result?.message);
        return false;
      }}
    >
      <FeedbackItems />
    </ModalForm>
  );
}
