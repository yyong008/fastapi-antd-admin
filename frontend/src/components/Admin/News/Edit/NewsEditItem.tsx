import {
  ProForm,
  ProFormDateTimePicker,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

export function NewsEditItem(props: any) {
  return (
    <>
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
        request={async () => {
          const ncs: any[] = props.newsCategory;
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
        style={{display:'none'}}
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
    </>
  );
}
