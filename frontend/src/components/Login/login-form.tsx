import { LoginForm, ProConfigProvider } from "@ant-design/pro-components";

import { ConfigProvider, } from "antd";

export function LoginFormWrap({ children }: any) {
  const handleSubmit = async (values: any) => {
    
  };

  return (
    <ProConfigProvider>
      <ConfigProvider
        theme={{
        }}
      >
        <div className="flex flex-col h-[100vh]  ">
          <LoginForm
            className="flex-1 text-slate-950"
            logo={
              <img
                alt="logo"
                src="/logo.png"
                style={{ borderRadius: "10px" }}
              />
            }
            title={"login-register.title"}
            subTitle={"login-register.desc"}
            initialValues={{
              autoLogin: true,
              username: "super admin",
              password: "123456",
            }}
            actions={[
              <div
                className="flex items-centermt-[20px] text-black"
                key="login-other"
              >
                <div>{"login-register.other-login"}</div>
                {/* <ActionIcons key="icons" /> */}
              </div>,
            ]}
            onFinish={async (values: string) => {
              await handleSubmit(values);
            }}
            submitter={{
              searchConfig: {
                submitText: "login-register.submit",
              },
            }}
          >
            {children}
          </LoginForm>
        </div>
      </ConfigProvider>
    </ProConfigProvider>
  );
}
