import { Button, Form, message } from "antd";
import {
  ModalForm,
  ProFormTextArea,
  ProFormUploadButton,
} from "@ant-design/pro-components";

import { EditOutlined } from "@ant-design/icons";
import { updateDocsFeedback } from "@/apis/admin/docs/feedback";
import { useState } from "react";

export default function FeedbackModal({ record, refetch }: any) {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      loading={loading}
      title={record?.id ? "修改反馈" : "创建反馈"}
      onOpenChange={(c) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={<Button type={"link"} icon={<EditOutlined />}></Button>}
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
          const url: string = values.file[0].response.data.name;
          data.url = url;
        }
        if (record.id) {
          data.id = record.id;
        }
        delete data.file;
        setLoading(true);
        const result: any = await updateDocsFeedback(record.id, data);
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
      <ProFormTextArea
        name="content"
        label="反馈内容"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormUploadButton
        label="反馈图片"
        name="file"
        placeholder="请输入名称"
        listType="picture-card"
        action="/api/upload"
        max={1}
        rules={[
          {
            required: false,
            message: "请上传",
          },
        ]}
      />
    </ModalForm>
  );
}
