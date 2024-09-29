import {
  DrawerForm,
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

import { createBlog } from "@/apis/admin/blog/blog";
import { message } from "antd";
import { useCategories } from "@/hooks/useCategories";
import { useNavigate } from "@tanstack/react-router";
import { useState } from "react";
import { useTags } from "@/hooks/useTags";

type BlogCreateFormProps = {
  categories: any;
  tags: any;
  trigger: any;
  content: string;
};

export function BlogCreateForm(props: BlogCreateFormProps) {
  const [form] = ProForm.useForm();
  const [loading, setLoading] = useState(false);
  const { categories, tags } = props;
  const nav = useNavigate();

  const categoriesOptions = useCategories(categories)
  const tagsOptions = useTags(tags)

  const onFinish = async (v: any) => {
    setLoading(true);
    v.category_id = v.categoryId;
    v.tag_id = v.tagId;
    const result: any = await createBlog(v);
    setLoading(false);
    if (result?.code === 0) {
      message.success(result?.message);
      nav({
        to: `/admin/blog/result`,
        state: {
          title: v.title,
          id: result.data.id,
        } as any,
      });
      return true;
    }
    message.error(result?.message);
    return false;
  };
  return (
    <DrawerForm
      form={form}
      title="创建博客"
      submitter={{
        resetButtonProps: {
          style: {
            display: "none",
          },
        },
      }}
      trigger={props.trigger}
      onFinish={onFinish}
      loading={loading}
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
      <ProForm.Item
        style={{ display: "none" }}
        label="编写新闻"
        name="content"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
        initialValue={props.content}
      >
        <ProFormTextArea />
      </ProForm.Item>
    </DrawerForm>
  );
}
