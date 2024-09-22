import "@/components/Admin/Tools/MailDetail/styles.css";

import { Button, Space } from "antd";
import { Link, useParams } from "@tanstack/react-router";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { MailForm } from "@/components/Admin/Tools/MailDetail/mail-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/admin/tools/mail/$id")({
  component: MailDetailRoute,
});

export function MailDetailRoute() {
  const [content, setContent] = useState("");
  const { id } = useParams({ strict: false });
  const { data, isLoading } = {
    data: { list: [], total: 0 },
    isLoading: false,
  };

  useEffect(() => {
    setContent(data?.content);
  }, [data]);
  return (
    <PageContainer>
      <ProCard
        loading={isLoading}
        style={{ height: 600 }}
        title="发送邮件"
        tooltip="默认支持的邮箱服务包括：”QQ”、”163”、”126”、”iCloud”、”Hotmail”、”Yahoo”等"
        extra={
          <Space>
            <Link to={`/admin/tools/mail/list`}>
              <Button type="primary">查看所有模板</Button>
            </Link>
            <MailForm data={data} content={content} />
          </Space>
        }
      >
        <div style={{ height: "400px" }}>
          <QuillEditor
            initContent={data?.content}
            content={content}
            setContent={setContent}
          />
        </div>
      </ProCard>
    </PageContainer>
  );
}
