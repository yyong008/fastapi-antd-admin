import { DeleteIt } from "../delete-it";
import { DictItemModalUpdate } from "../update-dict-item-modal";
import { Space } from "antd";
import { StatusType } from "@/components/common/status-type";
import { formatDate } from "@/utils/utils";

export const createColumns = ({ refetch, dictId }: any ) => [
  {
    dataIndex: "key",
    title: "字典键",
  },
  {
    dataIndex: "value",
    title: "字典值",
  },
  {
    dataIndex: "description",
    title: "描述",
  },
  {
    dataIndex: "remark",
    title: "标记",
  },
  {
    dataIndex: "status",
    title: "状态",
    renderText(_: any, record: any) {
      return <StatusType status={record.status} />;
    },
  },
  {
    dataIndex: "createdAt",
    title: "创建时间",
    render(_: any, record: any) {
      return <div>{record.createdAt ? formatDate(record.createdAt) : "-"}</div>;
    },
  },
  {
    dataIndex: "updatedAt",
    title: "更新时间",
    render(_: any, record: any) {
      return <div>{record.updatedAt ? formatDate(record.updatedAt) : "-"}</div>;
    },
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_: any, record: any) {
      return (
        <Space>
          <DictItemModalUpdate dictId={dictId} refetch={refetch} key="create-dict-modal" record={record} />
          <DeleteIt
            record={record}
            refetch={refetch}
          />
        </Space>
      );
    },
  },
];
