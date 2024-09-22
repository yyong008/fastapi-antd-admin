import * as ic from "@ant-design/icons";

import { ProFormText } from "@ant-design/pro-components";

const { UserOutlined, LockOutlined } = ic;

type AccountLoginProps = {
  isRegister?: boolean;
};

export function AccountLogin(props: AccountLoginProps) {
  return (
    <>
      <ProFormText
        name="username"
        fieldProps={{
          size: "large",
          prefix: <UserOutlined />,
        }}
        placeholder={"login-register.placeholder.username"}
        rules={[
          {
            required: true,
            message: "login-register.message.username-message"!,
          },
        ]}
      />
      <ProFormText.Password
        name="password"
        fieldProps={{
          size: "large",
          prefix: <LockOutlined />,
        }}
        placeholder={"请输入密码"}
        rules={[
          {
            required: true,
            message: "login-register.message.password-message",
          },
        ]}
      />
      {props.isRegister ? (
        <ProFormText.Password
          name="passwordRe"
          fieldProps={{
            size: "large",
            prefix: <LockOutlined />,
          }}
          placeholder={"login-register.placeholder.password-re"}
          rules={[
            {
              required: true,
              message: "login-register.message.password-message-re",
            },
          ]}
        />
      ) : (
        <></>
      )}
    </>
  );
}
