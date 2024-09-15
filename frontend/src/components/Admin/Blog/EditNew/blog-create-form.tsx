import {
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { message } from "antd";
import { useMemo } from "react";
import { useNavigate } from "@tanstack/react-router";

export function BlogCreateForm() {
  const nav = useNavigate();
  const [createBlog, others] = [(args) => args, {isLoading: false}];
  const { data: categories = {} } = { data: {  list: [], total: 0 } };
  const { data: tags = {} } = { data: {  list: [], total: 0 } };

  const categoriesOptions = useMemo(() => {
    return (
      categories?.list?.map((c: any) => {
        return {
          label: c.name,
          value: c.id,
        };
      }) ?? []
    );
  }, [categories]);

  const tagsOptions = useMemo(() => {
    return (
      tags?.list?.map((c: any) => {
        return {
          label: c.name,
          value: c.id,
        };
      }) ?? []
    );
  }, [tags]);

  const onFinish = async (v: any) => {
    const result: any = await createBlog(v);
    if (result.data?.code !== 0) {
      message.error(result.data?.message);
      return false;
    }

    message.success(result.data?.message);
    nav({
      to: `/admin/blog/result`,
      // state: { title: v.title, id: result.data.data.id },
    });
    return true;
  };
  return (
    <ProForm
      submitter={{
        resetButtonProps: {
          style: {
            display: "none",
          },
        },
      }}
      onFinish={onFinish}
      loading={others.isLoading}
    >
      <ProFormText
        label="博客标题"
        name="title"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="博客作者"
        name="author"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormText
        label="博客来源"
        name="source"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormDateTimePicker
        label="博客发布时间"
        name="publishedAt"
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
        name="categoryId"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
        options={categoriesOptions}
      />
      <ProFormSelect
        label="标签"
        name="tagId"
        options={tagsOptions}
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormTextArea
        label="编写博客"
        name="content"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      ></ProFormTextArea>
    </ProForm>
  );
}
