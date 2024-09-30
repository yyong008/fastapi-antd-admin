import { Button, Form, message } from "antd";
import {
  ModalForm,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { EditOutlined } from "@ant-design/icons";
import { createProfileLink } from "@/apis/admin/profile/link/link";
import { useParams } from "@tanstack/react-router";
import { useState } from "react";

export function LinkModalCreate({ refetch }: any) {
  const [form] = Form.useForm();
  const { id: categoryId } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);

  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title={"创建链接"}
      onOpenChange={() => {}}
      loading={loading}
      trigger={
        <Button type={"primary"} icon={<EditOutlined />}>
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
        const vals = {
          ...values,
        };

        vals.categoryId = Number(categoryId);

        setLoading(true);
        const result: any = await createProfileLink(vals);
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
        label="链接名"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        name="url"
        label="链接地址"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
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
            message: "请输入",
          },
        ]}
      />
    </ModalForm>
  );
}
