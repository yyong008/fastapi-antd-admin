import { PageContainer, ProTable } from "@ant-design/pro-components";
import { Space, Tag } from "antd";
import { useEffect, useState } from "react";

import { ChangeLogCreateModal } from "@/components/Admin/Docs/ChangeLog/ChangeLogModalCreate";
import ChangeLogUpdateModal from "@/components/Admin/Docs/ChangeLog/ChangeLogModalUpdate";
import { DeleteIt } from "@/components/Admin/Docs/ChangeLog/delete-it";
import { FormatTime } from "@/components/common/format-time";
import { createFileRoute } from "@tanstack/react-router";
import { getDocsChangelog } from "@/apis/admin/docs/changelog";
import { useSearch } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/docs/change-log")({
  component: ChangeLogRoute,
});

const typeMap = {
  1: {
    color: "blue",
    text: "重大更新",
  },
  2: {
    color: "green",
    text: "功能更新",
  },
  3: {
    color: "volcano",
    text: "Bug 修复",
  },
};

export function ChangeLogRoute() {
  const params = useSearch({ strict: false });
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {

    const res: any = await getDocsChangelog({ ...page });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page]);


  const columns = [
    {
      dataIndex: "publish_version",
      title: "版本",
    },
    {
      dataIndex: "publish_name",
      title: "发布者",
    },
    {
      dataIndex: "type",
      title: "更新类型",
      render: (_: any, record: { type: 1 | 2 | 3 }) => (
        <Tag color={typeMap?.[record.type]?.color}>
          {typeMap?.[record.type]?.text}
        </Tag>
      ),
    },
    {
      dataIndex: "content",
      title: "发布内容",
      ellipsis: true,
    },
    {
      dataIndex: "url",
      title: "跳转链接",
      ellipsis: true,
      render(_: any, record: any) {
        return <a href={record.url}>{record.url}</a>;
      },
    },
    {
      dataIndex: "publish_time",
      title: "发布时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.publish_time} />;
      },
    },
    {
      dataIndex: "createdAt",
      title: "创建时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.createdAt} />;
      },
    },
    {
      dataIndex: "updatedAt",
      title: "更新时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.updatedAt} />;
      },
    },
    {
      dataIndex: "op",
      title: "操作",
      render(_: any, record: any) {
        return (
          <Space>
            <ChangeLogUpdateModal
              key="changelog-modal-modify"
              record={record}
              refetch={() => {}}
            />
            <DeleteIt record={record} title={""} refetch={() => {}} />
          </Space>
        );
      },
    },
  ];
  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="更新日志"
        size="small"
        search={false}
        dataSource={data?.list ?? []}
        loading={loading}
        columns={columns}
        toolBarRender={() => [
          <ChangeLogCreateModal
            key="changelog-modal-create"
            refetch={() => {}}
          />,
        ]}
        options={{
          reload: () => {},
        }}
        pagination={{
          total: data.total,
          pageSize: Number(params.pageSize ?? 10),
          onChange(page, pageSize) {
            setPage({ page, pageSize });
          },
        }}
      />
    </PageContainer>
  );
}
