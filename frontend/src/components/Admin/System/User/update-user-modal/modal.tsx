import { ResponseStatus } from "@/constants/status";
import { UpdateUserModalUI } from "./modal-ui";
import { UserModalFormItems } from "./modal-form-items";
import { message } from "antd";
import { updateUser } from "@/apis/admin/system/user";
import { genHashedPassword } from "@/utils/crypto-js";

type UpdateUserModalProps = {
  loading: boolean;
  reload: any;
  handleUpdate?: any;
  depts: any[];
  roles: any[];
  record: any;
};

export function UpdateUserModal(props: UpdateUserModalProps) {
  const { loading, reload, depts, roles, record } = props;
  console.log("record", record.name, record.roles)
  return (
    <UpdateUserModalUI
      initValue={record}
      loading={loading}
      reload={reload}
      modalProps={{
        styles: { maxHeight: "600px", overflowY: "auto" },
      }}
      handleUpdate={async (values: any, form: any) => {
        let avatar = "";

        if (values.file && values.file.length > 0) {
          const url: string = values.file[0].response.data.name;
          const prefix = "/uploads/";
          avatar = url.startsWith(prefix) ? url : `${prefix}${url}`;
        }

        if (!values.password) delete values.password;

        delete values.file;
        const vals = { ...values, avatar, id: record.id };
        if (vals.email === "") delete vals.email; // no empty string
        vals.password = genHashedPassword(vals.password);
        const result: any = await updateUser(record.id ,vals);
        if (result && result.code === ResponseStatus.S) {
          form.resetFields();
          props.reload();
          message.success(result?.message || "Success");
          return true;
        }

        message.error(result?.message || "Failed");
        return false;
      }}
      onOpenChange={(c: any, form: any) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
          dept: record?.department?.id,
        });
      }}
    >
      <UserModalFormItems depts={depts} roles={roles} />
    </UpdateUserModalUI>
  );
}
