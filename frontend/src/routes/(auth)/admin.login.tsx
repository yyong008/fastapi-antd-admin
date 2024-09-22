import { ConfigProvider, Tabs } from "antd";
import { ProConfigProvider, ProFormCheckbox } from "@ant-design/pro-components";
import { memo, useMemo, useState } from "react";

import { AccountLogin } from "@/components/Login/account-login";
import { LoginFormWrap } from "@/components/Login/login-form";
// import { MobileLogin } from "@/components/Login/mobile-login";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/(auth)/admin/login")({
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
      // {
      //   key: "mobile",
      //   disabled: true,
      //   label: "手机号登录",
      // },
    ];
  }, []);
  const RemeberMe = memo(function Re() {
    return (
      <div style={{ margin: "10px 0px" }} className="text-black">
        <ProFormCheckbox name="autoLogin">
          {"记住密码"}
        </ProFormCheckbox>
      </div>
    );
  });
  return (
    <div>
      <ProConfigProvider>
        <ConfigProvider>
          <div className="flex flex-col h-[100vh]  ">
            <LoginFormWrap>
              <Tabs
                activeKey={type}
                onChange={setType}
                centered
                items={items}
              />
              {type === "account" && <AccountLogin />}
              {/* {type === "mobile" && <MobileLogin />} */}
              <RemeberMe />
            </LoginFormWrap>
          </div>
        </ConfigProvider>
      </ProConfigProvider>
    </div>
  );
}
