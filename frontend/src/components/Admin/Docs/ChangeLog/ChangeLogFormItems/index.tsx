import { ProFormDateTimePicker, ProFormSelect, ProFormText, ProFormTextArea } from "@ant-design/pro-components"

export const ChangeLogFormItems = () => {
  return <>
    <ProFormText
        name="publish_version"
        label="版本"
        placeholder="请输入版本号"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormSelect
        name="type"
        label="更新类型"
        placeholder="更新类型"
        rules={[
          {
            required: true,
            message: "请选择",
          },
        ]}
        options={[
          {
            label: "重大更新",
            value: 1,
          },
          {
            label: "功能更新",
            value: 2,
          },
          {
            label: "修复Bug",
            value: 3,
          },
        ]}
      />
      <ProFormText
        name="publish_name"
        label="发布人"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormDateTimePicker
        name="publish_time"
        label="发布日期"
        placeholder="发布日期"
        rules={[
          {
            required: true,
            message: "发布日期",
          },
        ]}
      />
      <ProFormText
        name="url"
        label="跳转地址"
        placeholder="跳转地址"
        rules={[
          {
            required: false,
            message: "请输入",
          },
        ]}
      />
      <ProFormTextArea
        name="content"
        label="更新内容"
        placeholder="更新内容"
        rules={[
          {
            required: true,
            message: "请输入更新内容",
          },
        ]}
      />
  </>
}
