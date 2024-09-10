import { LockOutlined, MobileOutlined } from "@ant-design/icons";
import { ProFormCaptcha, ProFormText } from "@ant-design/pro-components";

import { message } from "antd";

export function MobileLogin() {
  return (
    <>
      <ProFormText
        fieldProps={{
          size: "large",
          prefix: <MobileOutlined />,
        }}
        name="phone"
        placeholder={"login-register.placeholder.phone"}
        rules={[
          {
            required: true,
            message: "login-register.message.phone-message",
          },
          {
            pattern: /^1\d{10}$/,
            message: "login-register.message.phone-format-message",
          },
        ]}
      />
      <ProFormCaptcha
        fieldProps={{
          size: "large",
          prefix: <LockOutlined />,
        }}
        captchaProps={{
          size: "large",
        }}
        placeholder={"login-register.message.code"}
        captchaTextRender={(timing: boolean, count: number) => {
          if (timing) {
            return `${count} ${"login-register.code.get-verification-code"}`;
          }
          return "login-register.code.get-verification-code";
        }}
        name="captcha"
        rules={[
          {
            required: true,
            message: "login-register.code.verification-code-message"!,
          },
        ]}
        onGetCaptcha={async () => {
          message.success("get-captcha-success");
        }}
      />
    </>
  );
}
