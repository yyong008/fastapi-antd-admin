import {
  PageContainer,
  ProCard,
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { createFileRoute } from "@tanstack/react-router";
import { message } from "antd";
import { useNavigate } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/news/edit")({
  component: NewsEditRoute,
});

export function NewsEditRoute() {
  const nav = useNavigate();
  const [createNews] = [(args) => args];
  const { data: newsCategoryList, isLoading } = {
    data: {
      list: [],
      total: 0,
    },
    isLoading: false,
  };
  return (
    <PageContainer>
      <ProCard loading={isLoading}>
        <ProForm
          onFinish={async (v) => {
            const result = await createNews(v);
            if (result.data?.code !== 0) {
              message.error(result.data?.message);
              return false;
            }
            message.success(result.data?.message);
            nav({
              to: `/admin/news/result`,
              state: {
                // title: v.title, id: result.data.data.id
              },
            });
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
              const ncs = newsCategoryList?.list || [];
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
