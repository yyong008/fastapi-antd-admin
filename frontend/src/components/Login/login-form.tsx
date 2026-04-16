import { ConfigProvider, message } from "antd";
import { LoginForm, ProConfigProvider } from "@ant-design/pro-components";
import {
  setLocalStorageRefreshToken,
  setLocalStorageToken,
} from "@/utils/localstorage";

import { genHashedPassword } from "@/utils/crypto-js";
import { login } from "@/apis/login";
import { useNavigate } from "@tanstack/react-router";

interface LoginFormWrapProps {
  children?: React.ReactNode;
  isSignup?: boolean;
  onSignup?: (values: any) => Promise<boolean>;
  actions?: React.ReactNode;
}

export function LoginFormWrap({ children, isSignup, onSignup, actions }: LoginFormWrapProps) {
  const navigate = useNavigate();
  const handleSubmit = async (values: any) => {
    if (isSignup && onSignup) {
      return await onSignup(values);
    }
    const data = {
      username: values.username,
      password: genHashedPassword(values.password),
    };
    const result: any = await login(data);
    if (result && result.code === 0 && result.data.access_token?.length > 0) {
      setLocalStorageToken(result.data.access_token);
      setLocalStorageRefreshToken(result.data.refresh_token);
      message.success(result.message);
      navigate({ to: `/admin/dashboard` });
    } else {
      message.error(result.message);
    }
    return true;
  };

  return (
    <ProConfigProvider>
      <ConfigProvider theme={{}}>
        <LoginForm
            className="flex-1 text-slate-950"
            logo={
              <img
                alt="logo"
                src="/logo.png"
                style={{ borderRadius: "10px" }}
              />
            }
            title={isSignup ? "用户注册" : "FastAPI Antd Admin"}
            subTitle={isSignup ? "请填写注册信息" : "一个基于 FastAPI React Antd 的全栈管理系统"}
            initialValues={isSignup ? {} : {
              autoLogin: true,
              username: "super admin",
              password: "123456",
            }}
            onFinish={async (values: string) => {
              await handleSubmit(values);
            }}
            submitter={{
              searchConfig: {
                submitText: isSignup ? "注册" : "登录",
              },
            }}
            actions={actions}
          >
            {children}
          </LoginForm>
      </ConfigProvider>
    </ProConfigProvider>
  );
}
