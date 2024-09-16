import { Button, Form, message } from "antd";
import {
  ModalForm,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { EditOutlined } from "@ant-design/icons";
import { useParams } from "@tanstack/react-router";

export function LinkModalCreate({ refetch }: any) {
  const [form] = Form.useForm();
  const { id } = useParams({ strict: false });
  const [createProfileLinkById, other] = [(args) => args, { isLoading: false }]; // todo

  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title={"创建链接"}
      onOpenChange={() => {}}
      loading={other.isLoading}
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

        if (id) {
          vals.categoryId = Number(id);
        }
        const result = await createProfileLinkById(vals);
        if (result.data?.code !== 0) {
          message.error(result.data?.message);
          return false;
        }
        message.success(result.data?.message);
        refetch();
        form.resetFields();
        return true;
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
