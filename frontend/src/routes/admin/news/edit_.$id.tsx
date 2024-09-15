import {
  PageContainer,
  ProCard,
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { createFileRoute } from '@tanstack/react-router'
import { message } from "antd";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute('/admin/news/edit/$id')({
  component: EditDetailRoute
})

export function EditDetailRoute() {
  const { id } = useParams({ strict: false });

  const { data: newsCategoryList } = { data: []}
  const { data, isLoading } = { data: { }, isLoading: true }; // useReadNewsByIdQuery({ id: Number(id) });
  const [updateNewsById] =[args => args]
  return (
    <PageContainer>
      <ProCard loading={isLoading}>
        <ProForm
          // initialValues={{ ...data, date: data?.publishedAt }}
          initialValues={{ ...data }}
          onFinish={async (v) => {
            const data = v;
            data.id = Number(id);
            const result = await updateNewsById(data);
            if (result.data?.code !== 0) {
              message.error(result.data?.message);
              return false;
            }
            message.success(result.data?.message);
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
              const ncs: any[] = newsCategoryList || [];
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
