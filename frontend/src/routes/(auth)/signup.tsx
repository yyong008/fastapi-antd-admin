import { ConfigProvider } from "antd";
import { ProConfigProvider } from "@ant-design/pro-components";
import { LoginFormWrap } from "@/components/Login/login-form";
import { createFileRoute, Link, useNavigate } from "@tanstack/react-router";
import { ProFormText } from "@ant-design/pro-components";
import { UserOutlined, MailOutlined, LockOutlined } from "@ant-design/icons";
import { message } from "antd";
import { register } from "@/apis/login";
import { genHashedPassword } from "@/utils/crypto-js";

export const Route = createFileRoute("/(auth)/signup")({
  component: SignupComponent,
});

function SignupComponent() {
  const navigate = useNavigate();

  const handleSignup = async (values: any) => {
    if (values.password !== values.confirmPassword) {
      message.error("两次密码输入不一致");
      return false;
    }
    try {
      const data = {
        username: values.username,
        password: genHashedPassword(values.password),
        email: values.email,
      };
      const result: any = await register(data);
      if (result && result.code === 0) {
        message.success("注册成功，请登录");
        navigate({ to: `/login` });
      } else {
        message.error(result?.message || "注册失败");
      }
    } catch (error) {
      message.error("注册失败");
    }
    return true;
  };

  const actions = (
    <div className="text-center text-gray-600">
      已有账号？<Link to="/login" className="text-blue-500 hover:text-blue-600">立即登录</Link>
    </div>
  );

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-indigo-100 to-purple-100">
      <ProConfigProvider>
        <ConfigProvider>
          <LoginFormWrap isSignup onSignup={handleSignup} actions={actions}>
            <ProFormText
              name="username"
              placeholder="请输入用户名"
              rules={[{ required: true, message: "请输入用户名" }]}
              fieldProps={{ size: "large", prefix: <UserOutlined /> }}
            />
            <ProFormText
              name="email"
              placeholder="请输入邮箱"
              rules={[
                { required: true, message: "请输入邮箱" },
                { type: "email", message: "请输入正确的邮箱格式" },
              ]}
              fieldProps={{ size: "large", prefix: <MailOutlined /> }}
            />
            <ProFormText.Password
              name="password"
              placeholder="请输入密码"
              rules={[{ required: true, message: "请输入密码" }]}
              fieldProps={{ size: "large", prefix: <LockOutlined /> }}
            />
            <ProFormText.Password
              name="confirmPassword"
              placeholder="请确认密码"
              rules={[{ required: true, message: "请确认密码" }]}
              fieldProps={{ size: "large", prefix: <LockOutlined /> }}
            />
          </LoginFormWrap>
        </ConfigProvider>
      </ProConfigProvider>
    </div>
  );
}
