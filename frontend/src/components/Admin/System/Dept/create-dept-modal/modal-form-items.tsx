import {
  ProFormDigit,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from "@ant-design/pro-components";

export function ModalFormItems({ options }: any) {
  return (
    <>
      <ProFormText
        name="name"
        label="部门名称"
        placeholder="请输入"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormDigit
        name="order_no"
        label="排序"
        placeholder="排序"
        rules={[
          {
            required: true,
            message: "请输入",
          },
        ]}
      />
      <ProFormSelect
        name="parent_department_id"
        label="父部门"
        placeholder="不修改无需填写"
        rules={[
          {
            required: false,
            message: "请输入密码",
          },
        ]}
        options={options || []}
      />
      <ProFormTextArea
        name="description"
        label="描述"
        placeholder="不修改无需填写"
        rules={[
          {
            required: false,
            message: "请输入密码",
          },
        ]}
      />
    </>
  );
}
