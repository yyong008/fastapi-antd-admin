import {
  DrawerForm,
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { message } from "antd";
import { updateBlogById } from "@/apis/admin/blog/blog";
import { useCategories } from "@/hooks/useCategories";
import { useNavigate } from "@tanstack/react-router";
import { useTags } from "@/hooks/useTags";

type BlogEditFormProps = {
  id: number;
  data: any;
  trigger: any;
  content: string;
  categories: any[];
  tags: any[];
};

export function BlogEditForm(props: BlogEditFormProps) {
  const nav = useNavigate();
  const [form] = ProForm.useForm();
  const [loading, setLoading] = useState(false);
  const { data, content, categories = [], tags = [] } = props;

  const categoriesOptions = useCategories(categories);
  const tagsOptions = useTags(tags);

  useEffect(() => {
    form.setFieldValue("content", content);
  }, [props.content]);

  return (
    <DrawerForm
      form={form}
      trigger={props.trigger}
      initialValues={{
        ...data,
        categoryId: data.categoryId,
      }}
      submitter={{
        resetButtonProps: {
          style: {
            display: "none",
          },
        },
      }}
      onFinish={async (v) => {
        setLoading(true);
        v.category_id = v.categoryId;
        v.tag_id = v.tagId;
        const result: any = await updateBlogById(props.id, v);
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
      }}
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
        name="published_at"
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
        label="编写博客"
        name="content"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
        initialValue={content}
      >
        <ProFormTextArea />
      </ProForm.Item>
    </DrawerForm>
  );
}
