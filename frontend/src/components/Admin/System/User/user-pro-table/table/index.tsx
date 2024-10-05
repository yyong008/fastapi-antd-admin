import { ProTable } from "@ant-design/pro-components";
import { createToolBarRender } from "../toolbar/create-toolbar-render";
import { createUserTableColumns } from "../columns/columns";
import { useColorPrimary } from "@/hooks/use-color-primary";
import { useState } from "react";

export function UserProTable(props: any) {
  const { data, isLoading, refetch, page, setPage, roles, depts } = props;
  const [selectedRow, setSelectedRow] = useState([]);
  const { colorPrimary } = useColorPrimary();

  return (
    <>
      <ProTable
        size="small"
        search={false}
        headerTitle="用户表"
        scroll={{ x: 1300 }}
        rowKey="id"
        loading={isLoading}
        showSorterTooltip
        rowSelection={{
          selectedRowKeys: selectedRow,
          onChange: (selectedRowKeys) => {
            setSelectedRow(selectedRowKeys as any);
          },
        }}
        toolBarRender={() =>
          createToolBarRender({
            selectedRow,
            setSelectedRow,
            depts,
            roles,
            reload: refetch,
          })
        }
        dataSource={data?.list || []}
        columns={
          createUserTableColumns({
            depts,
            roles,
            colorPrimary,
            reload: refetch,
          }) as any
        }
        options={{
          reload: refetch,
        }}
        pagination={{
          total: data?.total,
          current: page || 1,
          pageSize: page.pageSize || 10,
          onChange(_page, pageSize) {
            setPage((prev) => {
              return { ...prev, page: _page, pageSize }
            });
          },
        }}
      />
    </>
  );
}
