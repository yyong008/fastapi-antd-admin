import { Button, Form, message } from "antd";

import { ChangeLogFormItems } from "../ChangeLogFormItems";
import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { updateDocsChangelogById } from "@/apis/admin/docs/changelog";
import { useState } from "react";

export default function ChangeLogUpdateModal({ record, refetch }: any) {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title="更新日志"
      loading={loading}
      onOpenChange={(c) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={<Button type="link" icon={<EditOutlined />}></Button>}
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        const data = { ...values };
        if (record.id) {
          data.id = record.id;
        }
        setLoading(true);
        const result: any = await updateDocsChangelogById(record.id, data);
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
      <ChangeLogFormItems />
    </ModalForm>
  );
}
