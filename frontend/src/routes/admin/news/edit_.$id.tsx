import {
  PageContainer,
  ProCard,
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { createFileRoute } from '@tanstack/react-router'
import { getNewsById } from "@/apis/admin/news/news";
import { message } from "antd";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute('/admin/news/edit/$id')({
  component: EditDetailRoute
})

export function EditDetailRoute() {
  const { id } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({});

  const getData = async () => {
    const res: any = await getNewsById(Number(id));
    if (res && res.code === 0) {

      setLoading(false);
      setData(res.data);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page, id]);
  return (
    <PageContainer>
      <ProCard loading={loading}>
        <ProForm
          initialValues={{ ...data }}
          onFinish={async () => {
            // const data = v;
            // data.id = Number(id);
            // const result = await updateNewsById(data);
            // if (result.data?.code !== 0) {
            //   message.error(result.data?.message);
            //   return false;
            // }
            // message.success(result.data?.message);
            return true;
          }}
        >
          <ProFormText
            label="新闻标题"
            name="title"
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          />
          <ProFormText
            label="新闻作者"
            name="author"
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          />
          <ProFormText
            label="新闻来源"
            name="source"
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          />
          <ProFormDateTimePicker
            label="新闻发布时间"
            name="date"
            width={"100%" as any}
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          />
          <ProFormSelect
            label="分类"
            name="newsId"
            request={async () => {
              const ncs: any[] = [];
              return ncs?.map((c: any) => {
                return {
                  label: c.name,
                  value: c.id,
                };
              }) as any;
            }}
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          />
          <ProForm.Item
            label="编写新闻"
            name="content"
            rules={[
              {
                required: true,
                message: "请输入",
              },
            ]}
          >
            <ProFormTextArea />
          </ProForm.Item>
        </ProForm>
      </ProCard>
    </PageContainer>
  );
}
