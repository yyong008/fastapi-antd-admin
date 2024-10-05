import { CreateUserModalUI } from "./modal-ui";
import { UserModalFormItems } from "./modal-form-items";
import { createUser } from "@/apis/admin/system/user";
import { ResponseStatus } from "@/constants/status";
import { message } from "antd";
import { genHashedPassword } from "@/utils/crypto-js"

type CreateUserModalProps = {
  loading?: boolean;
  reload: any;
  handleCreate?: any;
  depts: any[];
  roles: any[];
};

export function CreateUserModal(props: CreateUserModalProps) {
  const { loading, depts, roles, ...rest } = props;
  return (
    <CreateUserModalUI
      {...rest}
      modalProps={{
        style: { maxHeight: "600px", overflowY: "auto" },
      }}
      loading={loading || false}
      handleCreate={async (values: any, form: any) => {
        let avatar = "";

        if (values.file && values.file.length > 0) {
          const url: string = values.file[0].response.data.name;
          const prefix = "/uploads/";
          avatar = url.startsWith(prefix) ? url : `${prefix}${url}`;
        }
        if (!values.password) {
          delete values.password;
        }
        delete values.file;
        const vals = { ...values, avatar };
        if (vals.email === "") {
          delete vals.email; // no empty string
        }
        values.password = genHashedPassword(values.password);
        const result: any = await createUser(vals);
        if (result && result.code === ResponseStatus.S) {
          message.success(result?.message);

          form.resetFields();
          props.reload();
          return true
        }
        message.error(result?.message);
        return false
      }}
    >
      <UserModalFormItems depts={depts} roles={roles} />
    </CreateUserModalUI>
  );
}
