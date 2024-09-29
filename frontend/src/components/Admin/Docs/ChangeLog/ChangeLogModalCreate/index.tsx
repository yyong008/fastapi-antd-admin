import { Button, Form, message } from "antd";

import { ChangeLogFormItems } from "../ChangeLogFormItems";
import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { createDocsChangelog } from "@/apis/admin/docs/changelog";
import { useState } from "react";

export function ChangeLogCreateModal({ refetch }: any) {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      loading={loading}
      title="创建日志"
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
        setLoading(true);
        const result: any = await createDocsChangelog(values);
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
