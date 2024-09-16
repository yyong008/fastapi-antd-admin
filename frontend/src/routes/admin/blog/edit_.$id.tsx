import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { BlogEditForm } from '@/components/Admin/Blog/EditDetail/blog-edit-form';
import { createFileRoute } from '@tanstack/react-router'
import { getBlogById } from "@/apis/admin/blog/category";
import { message } from "antd";
import { useParams } from "@tanstack/react-router";

export const Route = createFileRoute('/admin/blog/edit/$id')({
  component:BlogEditDetailRoute
})

export function BlogEditDetailRoute() {
  const { id } = useParams({ strict: false });
  const [loading, setLoading] = useState(false);
  const [page] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({});

  const getData = async () => {
    const res: any = await getBlogById(Number(id));
    if (res && res.code === 0) {

      setLoading(false);
      setData(res.data);
    }
  };

  useEffect(() => {
    setLoading(true)
    getData();
  }, [page, id]);
  return (
    <PageContainer>
      <ProCard loading={loading}>
        <BlogEditForm
          loading={loading}
          data={data || {}}
          onFinish={async () => {
            // const values = v;
            // if (id) values.id = Number(id);
            // const data = {
            //   type: "",
            //   data: {
            //     ...values,
            //   },
            // };
            // const result: any = await updateBlog(data);

            // if (result.data && result.data.code === 1) {
            //   message.error(result.data.message);
            //   return false;
            // } else {
            //   message.success(result.data.message);
            //   return true;
            // }
          }}
        />
      </ProCard>
    </PageContainer>
  );
}
