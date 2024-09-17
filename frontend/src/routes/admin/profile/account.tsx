import {
  PageContainer,
  ProCard,
  ProForm,
  ProFormDigit,
  ProFormText,
} from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { createFileRoute } from '@tanstack/react-router'
import { getProfileAccount } from "@/apis/admin/profile/account";

export const Route = createFileRoute('/admin/profile/account')({
  component: ProfileAccountRoute
})

export function ProfileAccountRoute() {
  const [form] = ProForm.useForm();
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({});

  const getData = async () => {

    const res: any = await getProfileAccount();

    if (res && res.code === 0) {
      setData(res.data);
      form.setFieldsValue({
        name: res.data.name,
        nickname: res.data.nickname,
        email: res.data.email,
        remark: res.data.remark,
        theme: res.data.theme,
        lang: res.data.lang,
        phone: res.data.phone,
        createdAt: res.data.createdAt,
        department: res.data?.department?.name,
      });
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page]);
  return (
    <PageContainer>
      <ProCard loading={loading}>
        <ProForm
          form={form}
          readonly={true}
          layout="horizontal"
          labelCol={{ span: 1.7 }}
          submitter={false}
        >
          {/* <ProFormUploadButton
            name="file"
            label="用户头像"
            max={2}
            fieldProps={{
              name: "file",
              listType: "picture-card",
            }}
            action="/uploads"
          /> */}
          <ProFormText label="用户名" name="name" />
          <ProFormText label="昵称" name="nickname" />
          <ProFormText label="邮箱" name="email" />
          <ProFormText label="备注" name="remark" />
          <ProFormText label="语言" name="theme" />
          <ProFormText label="主题" name="lang" />
          <ProFormDigit label="手机号" name="phone" />
          <ProFormText label="创建时间" name="createdAt" />
          <ProFormText label="部门" name="department" />
        </ProForm>
      </ProCard>
    </PageContainer>
  );
}
