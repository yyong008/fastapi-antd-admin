import { Button, Form, message } from "antd";
import {
  ModalForm,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { EditOutlined } from "@ant-design/icons";
import { udpateProfileLinkCategoryById } from "@/apis/admin/profile/link/category";
import { useState } from "react";

export function LinkCategoryModalUpdate({ record, refetch }: any) {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title="修改Link分类"
      initialValues={{
        ...record,
      }}
      onOpenChange={() => {}}
      trigger={<Button type="link" icon={<EditOutlined />}></Button>}
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      loading={loading}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        setLoading(true);
        const result: any = await udpateProfileLinkCategoryById(record.id, values);
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
      <ProFormText
        name="name"
        label="标签名"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入用户名",
          },
        ]}
      />
      <ProFormTextArea
        name="description"
        label="描述"
        placeholder="请输入"
        rules={[
          {
            required: false,
            message: "请输入用户名",
          },
        ]}
      />
    </ModalForm>
  );
}
