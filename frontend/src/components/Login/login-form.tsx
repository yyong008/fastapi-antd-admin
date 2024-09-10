import { ConfigProvider, message, } from "antd";
import { LoginForm, ProConfigProvider } from "@ant-design/pro-components";
import { setLocalStorageRefreshToken, setLocalStorageToken } from "@/utils/localstorage";

import { genHashedPassword } from "@/utils/crypto-js";
import { login } from "@/apis/login";
import { useNavigate } from "@tanstack/react-router";

export function LoginFormWrap({ children }: any) {
  const navigate = useNavigate()
  const handleSubmit = async (values: any) => {
   const data = {
      username: values.username,
      password: genHashedPassword(values.password),
    };
    const result: any = await login(data);
    if (result && result.code === 0 && result.data.access_token?.length > 0) {
      setLocalStorageToken(result.data.access_token);
      setLocalStorageRefreshToken(result.data.refresh_token);
      message.success(result.message);
      navigate({ to: `/admin/dashboard`});
    } else {
      message.error(result.message);
    }
    return true;
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
