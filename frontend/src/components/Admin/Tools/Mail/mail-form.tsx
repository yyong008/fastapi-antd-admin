import { Button, Form, message } from "antd";
import {
  DrawerForm,
  ProFormDigit,
  ProFormText,
} from "@ant-design/pro-components";
import { SaveOutlined, SendOutlined } from "@ant-design/icons";
import { createMail, sendMail } from "@/apis/admin/tools/mail";

import { useState } from "react";

export function MailForm({ content, refetch }: any) {
  const [form] = Form.useForm();
  const [saveTplLoading, setSaveTplLoading] = useState(false)
  const [sendMailLoading, setSendMailLoading] = useState(false)

  const getFormData = () => {
    const vals = {
      subject: form.getFieldValue("subject"),
      to: form.getFieldValue("to"),
      content,
      host: form.getFieldValue("host"),
      port: form.getFieldValue("port"),
      user: form.getFieldValue("user"),
      pass: form.getFieldValue("pass"),
    };
    return vals;
  };

  const onSaveTemplate = async () => {
    if (!content) {
      return message.error("input email content ~");
    }

    const vals = getFormData();
    setSaveTplLoading(true)
    const result: any = await createMail(vals);
    setSaveTplLoading(false)
    if (result && result?.code === 0) {
      message.success(result?.message);
      refetch?.();
      form.resetFields();
      return true;
    }
    message.error(result?.message);
      return false;
  };

  const onSendMail = async () => {
    const vals = getFormData();
    setSendMailLoading(true)
    const result: any = await sendMail(vals);
    setSendMailLoading(false)
    if (result && result?.code === 0) {
      message.success(result?.message);
      refetch?.();
      return true;
    }

    message.error(result?.message);
    return false;
  };

  return (
    <DrawerForm
      title="编辑邮件信息"
      form={form}
      submitter={{
        render: (props) => {
          return [
            <Button
              loading={saveTplLoading}
              type="primary"
              key="rest"
              onClick={() => {
                onSaveTemplate();
              }}
            >
              保存模板<SaveOutlined />
            </Button>,
            <Button
              loading={sendMailLoading}
              type="primary"
              key="submit"
              onClick={() => {
                props.form?.submit?.();
              }}
            >
              发送邮件 <SendOutlined />
            </Button>,
          ];
        },
      }}
      onFinish={async () => {
        onSendMail();
      }}
      trigger={<Button type="primary">发送邮件<SendOutlined /></Button>}
    >
      <ProFormText
        label="邮件标题"
        name="subject"
        placeholder="请输入邮件主题"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="接收邮件人"
        name="to"
        placeholder="输入邮箱接收者"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="Host"
        name="host"
        placeholder="请输入邮箱 host 地址，例如 'smtp.163.com'"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormDigit
        label="端口"
        name="port"
        placeholder={"465"}
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="用户名"
        name="user"
        placeholder="邮箱地址"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="密码"
        placeholder="输入授权码或密码"
        tooltip="授权码可能需要开通 POP3/SMTP/IMAP"
        name="pass"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
    </DrawerForm>
  );
}
