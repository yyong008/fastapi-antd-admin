import { ConfigProvider, Tabs } from "antd";
import { ProConfigProvider, ProFormCheckbox } from "@ant-design/pro-components";
import { Link } from "@tanstack/react-router";
import { memo, useMemo, useState } from "react";

import { AccountLogin } from "@/components/Login/account-login";
import { LoginFormWrap } from "@/components/Login/login-form";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/(auth)/login")({
  component: LoginComponent,
});

function LoginComponent() {
  const [type, setType] = useState<string>("account");
  const items = useMemo(() => {
    return [
      {
        key: "account",
        label: "账户登录",
      },
    ];
  }, []);
  const RemeberMe = memo(function Re() {
    return (
      <div style={{ margin: "10px 0px" }} className="text-black">
        <ProFormCheckbox name="autoLogin">{"记住密码"}</ProFormCheckbox>
      </div>
    );
  });
  const actions = (
    <div className="text-center text-gray-600">
      还没有账号？<Link to="/signup" className="text-blue-500 hover:text-blue-600">立即注册</Link>
    </div>
  );

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-indigo-100 to-purple-100">
      <ProConfigProvider>
        <ConfigProvider>
          <LoginFormWrap actions={actions}>
              <Tabs
                activeKey={type}
                onChange={setType}
                centered
                items={items}
              />
              {type === "account" && <AccountLogin />}
              <RemeberMe />
            </LoginFormWrap>
        </ConfigProvider>
      </ProConfigProvider>
    </div>
  );
}
