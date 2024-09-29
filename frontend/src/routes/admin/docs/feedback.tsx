import { PageContainer, ProTable } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { FeedbackModalCreate } from "@/components/Admin/Docs/Feedback/FeedbackModalCreate";
import { createFeedbackColumns } from "@/components/Admin/Docs/Feedback/FeedbackColumns";
import { createFileRoute } from "@tanstack/react-router";
import { getDocsFeedback } from "@/apis/admin/docs/feedback";

export const Route = createFileRoute("/admin/docs/feedback")({
  component: FeedbackRoute,
});

export function FeedbackRoute() {
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
    const res: any = await getDocsFeedback({ ...page });

    if (res && res.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);

  return (
    <PageContainer>
      <ProTable
        rowKey="id"
        headerTitle="反馈内容"
        size="small"
        search={false}
        loading={loading}
        dataSource={data?.list ?? []}
        columns={createFeedbackColumns({ refetch: getData })}
        options={{
          reload: getData,
        }}
        toolBarRender={() => [
          <FeedbackModalCreate
            key="changelog-modal-create"
            refetch={getData}
          />,
        ]}
        pagination={{
          total: data?.total || 0,
          pageSize: page.pageSize || 10,
          onChange(page, pageSize) {
            setPage({ page, pageSize });
          },
        }}
      />
    </PageContainer>
  );
}
