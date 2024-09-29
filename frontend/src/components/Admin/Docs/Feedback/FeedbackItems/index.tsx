import {
  ProFormTextArea,
  ProFormUploadButton,
} from "@ant-design/pro-components";

export const FeedbackItems = () => {
  return (
    <>
      <ProFormTextArea
        name="content"
        label="反馈内容"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormUploadButton
        label="反馈图片"
        name="file"
        placeholder="请输入名称"
        listType="picture-card"
        action="/api/upload"
        max={1}
        rules={[
          {
            required: false,
            message: "请上传",
          },
        ]}
      />
    </>
  );
};
